import logging
import yaml
import SimpleITK as sitk
from SimpleITK.SimpleITK import Image

with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())
logging.config.dictConfig(config)
logger = logging.getLogger(__name__)


class ImageProcessor:
    """
    this class receive a sitk Image object and provide filter handlers
    and export function.
    """

    def __init__(self, image):

        self.image = image

        self.image_numpy_array = self.get_image_numpy_array()

    def get_image(self):
        return self.image

    def get_image_numpy_array(self):
        if isinstance(self.image, Image):
            return sitk.GetArrayFromImage(self.image)
        return None

    def denoising_handler(self, output_file, time_step=0.125, number_of_iterations=5, export=True):
        denoiser = sitk.CurvatureFlowImageFilter()

        denoiser.SetTimeStep(time_step)
        denoiser.SetNumberOfIterations(number_of_iterations)

        denoised_image = denoiser.Execute(self.image)
        if export:
            return self.__export_file__(denoised_image, output_file)
        return denoised_image

    def edge_filtering_handler(self, output_file, export=True):
        edge_detector = sitk.SobelEdgeDetectionImageFilter()
        edges_image = edge_detector.Execute(self.image)
        if export:
            return self.__export_file__(edges_image, output_file)
        return edges_image

    def gaussian_blur_handler(self, output_file, sigma=1.5, export=True):
        blurrer = sitk.DiscreteGaussianImageFilter()
        blurrer.SetVariance(sigma)
        logger.info("Execute blur func")
        blurred_image = blurrer.Execute(self.image)

        if export:
            return self.__export_file__(blurred_image, output_file)
        return blurred_image

    def thresholding_handler(self, output_file, lower_threshold=100, upper_threshold=200, inside=1, outside=0,
                             export=True):
        threshold_filter = sitk.BinaryThresholdImageFilter()
        threshold_filter.SetLowerThreshold(lower_threshold)
        threshold_filter.SetUpperThreshold(upper_threshold)
        threshold_filter.SetInsideValue(inside)
        threshold_filter.SetOutsideValue(outside)
        thresholded_image = threshold_filter.Execute(self.image)
        if export:
            return self.__export_file__(thresholded_image, output_file)
        return thresholded_image

    def resampling_handler(self, output_file, new_spacing=(1.0, 1.0, 1.0), export=True):

        original_spacing = self.image.GetSpacing()
        original_size = self.image.GetSize()

        new_size = [
            int(round(original_size[0] * (original_spacing[0] / new_spacing[0]))),
            int(round(original_size[1] * (original_spacing[1] / new_spacing[1]))),
            int(round(original_size[2] * (original_spacing[2] / new_spacing[2])))
        ]
        resampler = sitk.ResampleImageFilter()

        resampler.SetSize(new_size)
        resampler.SetOutputSpacing(new_spacing)
        resampler.SetOutputOrigin(self.image.GetOrigin())
        resampler.SetOutputDirection(self.image.GetDirection())
        resampler.SetTransform(sitk.Transform())
        resampler.SetDefaultPixelValue(0)
        resampler.SetInterpolator(sitk.sitkLinear)

        resampled_image = resampler.Execute(self.image)

        if export:
            return self.__export_file__(resampled_image, output_file)
        return resampled_image

    def rescaling_handler(self, output_file, output_minimun=-1000, output_maximun=1000, export=True):
        rescaler = sitk.RescaleIntensityImageFilter()

        rescaler.SetOutputMinimum(output_minimun)
        rescaler.SetOutputMaximum(output_maximun)
        logger.info("Execute rescale func")
        rescaled_image = rescaler.Execute(self.image)
        if export:
            return self.__export_file__(rescaled_image, output_file)
        return rescaled_image

    def intensity_normalisation_handler(self, output_file, export=True):
        statistics_filter = sitk.StatisticsImageFilter()
        statistics_filter.Execute(self.image)
        mean_intensity = statistics_filter.GetMean()
        std_deviation = statistics_filter.GetSigma()
        normalized_image = sitk.Cast((self.image - mean_intensity) / std_deviation, sitk.sitkFloat32)
        if export:
            return self.__export_file__(normalized_image, output_file)
        return normalized_image

    @classmethod
    def __export_file__(cls, image, output_file):
        sitk.WriteImage(image, output_file)

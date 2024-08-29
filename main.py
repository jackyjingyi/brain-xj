import logging.config
import os.path
import yaml
import logging
import argparse
import SimpleITK as sitk
from image_processor import ImageProcessor


def main():
    # create ArgumentParser ob
    parser = argparse.ArgumentParser(description="Process MRI data.")

    # add file input argument
    parser.add_argument("--input", required=True, help="Input NIfTI file path.")

    # add file output argument
    parser.add_argument("--output", required=True, help="Output NIfTI file path.")

    # add filter type
    parser.add_argument("--filter", default='blur', help="Filter type (default: blur).")

    # add sigma argument
    parser.add_argument("--blur-sigma", type=float, default=1.5, help="Sigma value for the filter (default: 1.5).")

    # add time step
    parser.add_argument("--dn-ts", type=float, default=0.125, help="Time_step value for denoise filter.")

    # add number_of_iterations for denoise filter
    parser.add_argument("--dn-noi", type=int, default=5, help="Number_of_iterations value for denoise filter")

    # add arguments for threshold func
    parser.add_argument("--th-lower", type=int, default=100, help="Lower_threshold value for threshold filter")
    parser.add_argument("--th-upper", type=int, default=200, help="Upper_threshold value for threshold filter")
    parser.add_argument("--th-inside", type=int, default=1, help="inside value for threshold filter")
    parser.add_argument("--th-outside", type=int, default=0, help="outside value for threshold filter")

    # add arguments for rescale filter func
    parser.add_argument("--rsc-outmin", type=int, default=-1000, help="Lower_threshold value for threshold filter")
    parser.add_argument("--rsc-outmax", type=int, default=1000, help="Lower_threshold value for threshold filter")

    # store argument
    args = parser.parse_args()
    logger.info(args)

    if not os.path.exists(args.input):
        raise FileNotFoundError(f"The file '{args.input}' does not exist.")

    # list of str contains processes
    process_seq = args.filter.split('-')

    cnt = 0
    n = len(process_seq)
    image = sitk.ReadImage(args.input)
    while cnt < n:
        # create new instance each iteration
        process_handler = ImageProcessor(image)
        if process_seq[cnt] == 'blur':
            image = process_handler.gaussian_blur_handler(args.output, sigma=args.blur_sigma, export=False)
        elif process_seq[cnt] == 'resample':
            image = process_handler.resampling_handler(args.output, export=False)
        elif process_seq[cnt] == 'rescale':
            image = process_handler.rescaling_handler(args.output, output_maximun=args.rsc_outmax,
                                                      output_minimun=args.rsc_outmin, export=False)
        elif process_seq[cnt] == 'denoise':
            image = process_handler.denoising_handler(args.output, export=False)
        elif process_seq[cnt] == 'norm':
            image = process_handler.intensity_normalisation_handler(args.output, export=False)
        elif process_seq[cnt] == 'edge':
            image = process_handler.edge_filtering_handler(args.output, export=False)
        elif process_seq[cnt] == 'threshold':
            image = process_handler.thresholding_handler(args.output, lower_threshold=args.th_lower,
                                                         upper_threshold=args.th_upper, inside=args.th_inside,
                                                         outside=args.th_outside,
                                                         export=False)
        cnt += 1
    ImageProcessor.__export_file__(image, args.output)


if __name__ == '__main__':
    with open('logging_config.yaml', 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
    logger = logging.getLogger(__name__)

    main()

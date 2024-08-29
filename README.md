
The project is designed to transform medical sacn by user's command.

main process is showed below<br /> <br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/32575044/1724907500564-9a714c45-6076-4bdf-8cb5-cf1655ff8b48.png#averageHue=%23fefefe&clientId=u0abd35ae-64d8-4&from=paste&height=797&id=uc61760ae&originHeight=797&originWidth=1012&originalType=binary&ratio=1&rotation=0&showTitle=false&size=21140&status=done&style=none&taskId=u91423657-13d4-4154-a9a0-e7fef2d9abc&title=&width=1012)<br />script example is
```python
 python main.py --input ./test_data/sub-0002_ses-01_T1w.nii.gz --output processed_output12.nii.gz --filter blur-rescale --rsc-outmin -800 --rsc-outmax 1200
```

input parameters are

| name | type  | desc | default value |
| --- | --- | --- | --- |
| --input | str | Input NIfTI file path | <br /> |
| --output | str | Output NIfTI file path. | <br /> |
| --filter | str | accept "blur,resample,rescale,denoise,norm,edge,threshold", <br />if a chain process is needed, enter filter name and sepreate with "-", for instance "blur-resample-rescale",<br /> | <br /> |
| --blur-sigma  | float | Sigma value for the blur filter | 1.5 |
| --dn-ts | float | Time_step value for denoise filter. | 0.125 |
| --dn-noi | int |  Number_of_iterations value for denoise filter. | 5 |
| --th-lower | int |  Lower_threshold value for threshold filter | 100 |
| --th-upper | int |  Upper_threshold value for threshold filter. | 200 |
| --th-inside | int | inside value for threshold filter | 1 |
| --th-outside | int | outside value for threshold filter | 0 |
| --rsc-outmin | int | rescale output_minimun value for rescaleing filter | -1000 |
| --rsc-outmax | int | rescale output_maximun value for rescaleing filter | 1000 |


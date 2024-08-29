
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

output display examples

blur filter
```shell
python main.py --input ./test_data/sub-0002_ses-01_T1w.nii.gz --output processed_outputblur.nii.gz --filter blur 
```
origin										blur<br />![image.png](https://cdn.nlark.com/yuque/0/2024/png/32575044/1724912957358-767d8416-49b5-4bf5-9d01-30572b2a384e.png#averageHue=%232a2a2a&clientId=u0abd35ae-64d8-4&from=paste&height=1098&id=u18ae01ea&originHeight=1098&originWidth=1384&originalType=binary&ratio=1&rotation=0&showTitle=false&size=459406&status=done&style=none&taskId=u70c1ae60-c946-4fc7-8e3b-2f9d94c6eaf&title=&width=1384) <br />chain function
```shell
 python main.py --input ./test_data/sub-0002_ses-01_T1w.nii.gz --output processed_outputchain.nii.gz --filter blur-rescale --rsc-outmin -800 --rsc-outmax 1200
```
![image.png](https://cdn.nlark.com/yuque/0/2024/png/32575044/1724913081374-b3153c54-0320-443a-8633-305c5b7efdc7.png#averageHue=%232a2a2a&clientId=u0abd35ae-64d8-4&from=paste&height=1097&id=u8584baaa&originHeight=1097&originWidth=1401&originalType=binary&ratio=1&rotation=0&showTitle=false&size=461517&status=done&style=none&taskId=u0bf1a3b9-8698-404f-9824-79450004d8e&title=&width=1401)

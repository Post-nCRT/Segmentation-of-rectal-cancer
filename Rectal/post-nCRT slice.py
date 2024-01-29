import os,json
import SimpleITK as sitk
import numpy as np

import pandas as pd

patientid=[1,2,3,4,5,]#make patient id as a list,[1,2,3,4,5,] is a example
src_root="H:\\selected_4kinds_data\\t2_post"
j=1
k=1

id=[]
cntslice=[]
for dir in id:
    cnt=0
    subroot=os.path.join(src_root,str(dir),'lesion_patch_1')
    list = os.listdir(subroot)
    list.sort()
    print(list)
    for file in list:
        if file == 'mask.nii.gz':
            image_name = file
            image_file = os.path.join(subroot, file)
            labelimg = sitk.ReadImage(image_file)
            labelnp = sitk.GetArrayFromImage(labelimg)
            img = sitk.ReadImage(os.path.join(subroot, "main.nii.gz"))
            imgnp = sitk.GetArrayFromImage(img)
            x, y, z = labelimg.GetSize()
            cnt = 0
            for i in range(0, z):
                labelslicenp = labelnp[i, :, :]
                imageslicenp = imgnp[i, :, :]
                if np.sum(labelslicenp) == 0:
                    continue
                else:
                    labelslicenp = labelslicenp.reshape(1, labelslicenp.shape[0], labelslicenp.shape[1])
                    labelslice = sitk.GetImageFromArray(labelslicenp)
                    labelslice.SetOrigin(labelimg.GetOrigin())
                    labelslice.SetSpacing(labelimg.GetSpacing())
                    labelslice.SetDirection(labelimg.GetDirection())
                    sitk.WriteImage(labelslice,
                                    os.path.join("H:\\colonpostnopcrslice\\labelsTr", "colon_%04d" % j + ".nii.gz"))
                    j = j + 1
                    imageslicenp = imageslicenp.reshape(1, imageslicenp.shape[0], imageslicenp.shape[1])
                    imageslice = sitk.GetImageFromArray(imageslicenp)
                    imageslice.SetOrigin(img.GetOrigin())
                    imageslice.SetSpacing(img.GetSpacing())
                    imageslice.SetDirection(img.GetDirection())
                    sitk.WriteImage(imageslice,os.path.join("H:\\colonpostnopcrslice\\imagesTr", "colon_%04d" % k + ".nii.gz"))
                    k = k + 1
                    cnt = cnt + 1
            id.append(dir)
            cntslice.append(cnt)

data = pd.read_csv(r"H:\\colonnopcr.csv")
data['a'] = id
data['b'] = cntslice
data.to_csv(r'H:\\colonnopcr.csv', index=False)

import os

# texttofind = 'hat'
# texttoreplace = ''
sourcepath = os.listdir('C:/Users/suzan/Downloads/VOC2028/annotations/')

for file in sourcepath:
    inputfile = 'C:/Users/suzan/Downloads/VOC2028/annotations/'+file
    print('Conversion is ongoing for:'+ inputfile)
    with open(inputfile,'r') as inputfile:
        filedata = inputfile.read()
        # freq = 0
        # freq = filedata.count(texttofind)
    destinationpath = 'C:/Users/suzan/Downloads/VOC2028/withoutjpeg/' + file
    # filedata = filedata.replace('hat', 'helmet')
    # filedata = filedata.replace('person', 'no_helmet')
    filedata = filedata.replace('jpeg', 'jpg')
    with open(destinationpath,'w') as file:
        file.write(filedata)
    # print('Total %d Record Replaced' %freq)
    print('Replaced!')
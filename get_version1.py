
import os,win32api


#通过OS.walk获取文件夹所有指定文件，包括子文件夹中
def get_all_files(folder_path):
    path2 = {}
    path = []
    filenames = []
    for maindir, subdir,file_name_list in os.walk(folder_path):  #根目录下的每一个文件夹包含自己，产生3-元组，
        for filename in file_name_list:
            if filename.endswith(('.exe','.dll','.sys')):
                apath = os.path.join(maindir,filename)
                path.append(apath)
                filenames.append(filename)

                #合并两个字典，将字典传给get_version函数
                path1 = dict(zip(path, filenames))
                path2.update(path1)

    print(path2)
    return (path2)




def get_file_version1(folder_path):
    file_path = get_all_files(folder_path)
    i = 0
    dict2 ={}
    for key in file_path:

        pe_names = list(file_path.values())
        try:
            info = win32api.GetFileVersionInfo(key,'\\')
            ms = info['FileVersionMS']
            ls = info['FileVersionLS']
            version = '%d.%d.%d.%d' % (win32api.HIWORD(ms), win32api.LOWORD(ms), win32api.HIWORD(ls), win32api.LOWORD(ls))

            dict1 = {pe_names[i]: version}
            dict2.update(dict1)
            i=i+1
        except:
            print("the file no version:" + key)


    print(dict2)
    return dict2



#test = get_file_version1("C:\\Program Files (x86)\\COMODO\\test")
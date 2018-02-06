from MediaInfoDLL3 import *

def GetMediaInfo(inpath, isShow=False, isOut=False, outpath=None):
    MI = MediaInfo()
    MI.Open(inpath)
    inform = MI.Inform()
    MI.Close()
    if isShow:
        print(inform)
    if isOut:
        if outpath is None:
            outpath = '{path}.txt'.format(path=inpath)
        print('MediaInfo was saved in {path}'.format(path=outpath))
        with open(outpath, "w") as f:
            f.write(inform)
    return inform

def GetMediaInfoComplete(inpath, isShow=False, isOut=False, outpath=None):
    MI = MediaInfo()
    MI.Option_Static("Complete", "1")
    MI.Open(inpath)
    inform = MI.Inform()
    MI.Close()
    if isShow:
        print(inform)
    if isOut:
        if outpath is None:
            outpath = '{path}.txt'.format(path=inpath)
        print('MediaInfo was saved in {path}'.format(path=outpath))
        with open(outpath, "w") as f:
            f.write(inform)
    return inform

def GetMediaBitrate(path):
    MI = MediaInfo()
    MI.Open(path)
    return MI.Get(Stream.Video, 0, "BitRate")

def GetMediaColorSpace(path):
    MI = MediaInfo()
    MI.Open(path)
    return MI.Get(Stream.Video, 0, "ColorSpace")+MI.Get(Stream.Video, 0, "ChromaSubsampling").replace(':','')+'P'+MI.Get(Stream.Video, 0, "BitDepth")

def GetMediaMenu(path):
    MI = MediaInfo()
    MI.Open(path)
    return MI.Inform().split('\r\nMenu\r\n')[-1]

def GetMediaMenuList(path):
	MI = MediaInfo()
	MI.Open(path)
	menu_dict = {}
	menu_line_list = MI.Inform().split('\r\nMenu\r\n')[-1].split('\r\n')
	for menu_line in menu_line_list:
		line_list = menu_line[0:12], menu_line.split(':')[-1]
		if line_list[0].find(':') > 0:
			menu_dict[line_list[0]] = line_list[1]
	for key in menu_dict:
		print(key, '=>', menu_dict[key])
	return menu_dict

def GetMediaScanType(path, initial=False):
    MI = MediaInfo()
    MI.Open(path)
    scanType = MI.Get(Stream.Video, 0, "ScanType")
    if initial:
        scanType = scanType[0].lower()
    return scanType

def GetMediaScanOrder(path):
    MI = MediaInfo()
    MI.Open(path)
    return MI.Get(Stream.Video, 0, "ScanOrder")

def GetMediaDelay(path):
    MI = MediaInfo()
    MI.Open(path)
    return MI.Inform().split('\r\nDelay relative to video')[1].split('\r\n')[-1].split(': ')[1]

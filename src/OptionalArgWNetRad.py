import argparse
import time
import datetime
#bad_data_value = 6999
# import dp_funks
# For help from the command line, type either:
# python OptionalArg.py -h
# or 
# python OptionalArg.py --h
##################################################
# Run this file from Aptana Studio by typing:
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\array_Temperature.csv
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\array_Battery.csv -n 10 20
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\outputfile.csv
# AND by having ${string_prompt} ${string_prompt} ${string_prompt} in the run configuration argument list 
# (Don't forget to insert a space between the two string prompts in the run configuration.)
##################################################
# Run this code from the command line by typing:
# python CompareDatesTwoFiles.py 
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\array_Temperature.csv
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\array_Battery.csv -n 10 20
#C:\\bobs_folders\\py_datapro\\DataPro_Sample_Files\\outputs\\outputfile.csv
parser = argparse.ArgumentParser(description = 'reads first and last dates from two output files \n filename1 and filename2')
parser.add_argument("filename1", help="Directory and the first filename (This should be the raw rad file if the -netrad option is chosen)"\
                    , type =str)
parser.add_argument("filename2", help="Directory and the second filename (This should be the windspeed file if the -netrad option is chosen)"\
                    , type =str)
parser.add_argument("outputfile", help="Directory and the filename of the output file"\
                    , type =str)
parser.add_argument('-n','-N','-r','-R','--netrad','-netrad', help=" Two floating point decimals will need to follow this optional argument: \
    The first floating point value represents the multiplier for positive data values.  \
    The second floating point value represents the multiplier for negative data values. \
    Using the optional argument will cause the code  \
    to assume that filename1 is the raw radiation file and that filename2 is the windspeed file.  \
    WITHOUT this optional argument, filename1 and filename2 will just be glommed together"
    ,nargs =2  , type =float)
args = parser.parse_args()
try:
    print args.netrad[0]
    print args.netrad[1]
except:
    pass
ProcessNetRad = False
if args.netrad:
    print "time to process netrad\n"
    ProcessNetRad = True
else:
    print "not time to process netrad\n"
######### PROCESS first file
print "File being opened is: "
print args.filename1
first_file_object = open(args.filename1,'r')
data1 = first_file_object.readlines()
first_line_file1 = data1[4]
last_line_file1 = data1[-1]
first_line_file1 = first_line_file1.rstrip()
last_line_file1 = last_line_file1.rstrip()
first_line_file1_array= first_line_file1.split(',')
last_line_file1_array= last_line_file1.split(',')

print "\n"
print first_line_file1_array[0]
print "\n"
ymd=time.strptime(first_line_file1_array[0].strip('"').split()[0],'%Y-%m-%d')[0:3]
print "ymd: ", ymd;
print "\n"
hms=time.strptime(first_line_file1_array[0].strip('"').split()[1],'%H:%M:%S')[3:6]
print "hms: ", hms
print "\n"
YmdHmsStart1 = time.strptime(first_line_file1_array[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
print "YmdHmd1: ", YmdHmsStart1
print "\n"
YmdHmsEnd1 = time.strptime(last_line_file1_array[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
Start1 = datetime.datetime(YmdHmsStart1[0], YmdHmsStart1[1], YmdHmsStart1[2], YmdHmsStart1[3], YmdHmsStart1[4], YmdHmsStart1[5])
End1 = datetime.datetime(YmdHmsEnd1[0], YmdHmsEnd1[1], YmdHmsEnd1[2], YmdHmsEnd1[3], YmdHmsEnd1[4], YmdHmsEnd1[5])
first_date_str_file1 = first_line_file1_array[0].strip('"').split()[0].split('-')
last_date_str_file1 = last_line_file1_array[0].strip('"').split()[0].split('-')
##########################################PROCESS SECOND FILE
print "File being opened is: "
print args.filename2
second_file_object = open(args.filename2,'r')
data2 = second_file_object.readlines()
first_line_file2 = data2[4]
last_line_file2 = data2[-1]
first_line_file2 = first_line_file2.rstrip()
last_line_file2 = last_line_file2.rstrip()
first_line_file2_array= first_line_file2.split(',')
last_line_file2_array= last_line_file2.split(',')
first_date_str_file2 = first_line_file2_array[0].strip('"').split()[0].split('-')
last_date_str_file2 = last_line_file2_array[0].strip('"').split()[0].split('-')
YmdHmsStart2 = time.strptime(first_line_file2_array[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
YmdHmsEnd2 = time.strptime(last_line_file2_array[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
Start2 = datetime.datetime(YmdHmsStart2[0], YmdHmsStart2[1], YmdHmsStart2[2], YmdHmsStart2[3], YmdHmsStart2[4], YmdHmsStart2[5])
End2 = datetime.datetime(YmdHmsEnd2[0], YmdHmsEnd2[1], YmdHmsEnd2[2], YmdHmsEnd2[3], YmdHmsEnd2[4], YmdHmsEnd2[5])
############################################SUMMARIZE
if Start1 < Start2:
    print "first file starts before the second one\n"
    StartDateOutput = Start2
else:
    print "second file starts before or at the same time as the first one\n"
    StartDateOutput = Start1
if End1 < End2:
    print "first file ends before the second one\n"
    EndDateOutput = End1
else:
    print "second file ends before or at the same time as the first one\n"
    EndDateOutput = End2

DataWDatesToProcess = False
if StartDateOutput <= EndDateOutput:
    print "We can consolidate the files\n"
    DataWDatesToProcess = True
else:
    print args.filename1 
    print "\n and \n"
    print args.filename2
    print "\n do not have overlapping dates"
    DataWDatesToProcess = False
    
print "first file: \n"
print first_date_str_file1
print "\n"
print last_date_str_file1
print "\n"
print "second file: \n"
print first_date_str_file2
print "\n"
print last_date_str_file2
############     Pull DATA between StartDateOutPut and EndDateOutput 
############     from filename1 AND filename2
datafile1 = data1[4:]
datafile2 = data2[4:]
if DataWDatesToProcess:
    for line1 in datafile1:
        lineofdata1 = line1.rstrip()
        linearray1= lineofdata1.split(',')
        YmdHmsline1 = time.strptime(linearray1[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
        Timeline1 = datetime.datetime(YmdHmsline1[0],\
                YmdHmsline1[1],YmdHmsline1[2],YmdHmsline1[3],YmdHmsline1[4],YmdHmsline1[5])
        if ((Timeline1 < StartDateOutput) or (Timeline1 > EndDateOutput)):
                pass
        else:
            print YmdHmsline1 
            print linearray1[1]
            for line2 in datafile2:
                lineofdata2 = line2.rstrip()
                linearray2 = lineofdata2.split(',')
                YmdHmsline2 = time.strptime(linearray2[0].strip('"'),'%Y-%m-%d %H:%M:%S')[0:6]
                Timeline2 = datetime.datetime(YmdHmsline2[0],\
                        YmdHmsline2[1],YmdHmsline2[2],YmdHmsline2[3],YmdHmsline2[4],YmdHmsline2[5])
                if Timeline2 == Timeline1:
                    print linearray2[1]
                    print type(linearray2[1])
                else:
                    pass
                
else:
    pass
#######CLOSE FILES
first_file_object.flush()
first_file_object.close()
second_file_object.flush()
second_file_object.close()


import PyQt4.uic as uic
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description="Compile a Qt UI file")
    parser.add_argument( "--in_file","-i",dest='in_file',
            default="./app/test_app.ui", type=str,
            help="Specifiy a .ui file to compile into a py file")
    parser.add_argument("--out_file","-o", dest='out_file',
            default="./app/test_app.py", type=str,
            help="Specify the name of the resulting Python file")
    return parser

parsed = parse_args().parse_args()
print("Compiling {} into {}".format(parsed.in_file, parsed.out_file))
fpy = open(parsed.out_file,'w')
uic.compileUi(parsed.in_file, fpy)
fpy.close()

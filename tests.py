from bootcamp import get_dir_items
import os, shutil
from nose.tools import with_setup
import json

def setup_func():
	os.makedirs("/tmp/exampledir")
	os.makedirs("/tmp/exampledir/Sub_Dir")
	os.makedirs("/tmp/exampledir/Sub_Dir2")
	os.makedirs("/tmp/exampledir/Sub_Dir2/SubSubDir")
	open("/tmp/exampledir/File_Name.md", 'a').close()
	open("/tmp/exampledir/Sub_Dir/Sub_File_Name.md", 'a').close()
	open("/tmp/exampledir/Sub_Dir2/SubSubDir/Sub_Sub_File_Name.md", 'a').close()

def teardown_func():

	shutil.rmtree("/tmp/exampledir")

@with_setup(setup_func, teardown_func)
def test_get_menu_items():
	expected_output = [{"files": [{"files": [{"path": "/tmp/exampledir/Sub_Dir2/SubSubDir/", "orig": "Sub_Sub_File_Name", "cleaned": "Sub Sub File Name"}], "path": "/tmp/exampledir/Sub_Dir2/", "orig": "SubSubDir","cleaned": "SubSubDir"}], "path": "/tmp/exampledir/", "orig": "Sub_Dir2", "cleaned": "Sub Dir2"},{"path": "/tmp/exampledir/","orig": "File_Name","cleaned": "File Name"},{"files": [{"path": "/tmp/exampledir/Sub_Dir/","orig": "Sub_File_Name","cleaned": "Sub File Name"}],"path": "/tmp/exampledir","orig": "Sub_Dir","cleaned": "Sub Dir"}]

	items = get_dir_items("/tmp/exampledir")
	assert expected_output == items




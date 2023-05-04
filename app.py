from flask import Flask, render_template, request, redirect, send_file
from dotenv import load_dotenv

# import fileparsers
import os
import shutil
import datetime
import threading
import logging
import uuid
import time
import magic
# from astropy.table import Table

load_dotenv()
PATHBASE = os.path.abspath(os.path.dirname(__file__))

app = Flask('sysprac')


logger = logging.getLogger('webserver')
logging.basicConfig(level=logging.INFO,
    format='%(name)-10s %(levelname)-8s [%(asctime)s] %(message)s',
)

# ***************************************
# BEGIN server route definitions
# ***************************************


@app.route('/')
def landing_page():
    """Home page. User can upload files from here"""
    return render_template('landing.html')


def check_extension(file, ext):
    contents = file.read()
    # file.read() makes file pointer points to last position, make the file pointer to first position by using file.seek()
    file.seek(0)
    fileType = magic.from_buffer(contents)
    fileType = fileType.split(' ')[0].lower()
    if(fileType == ext):
        return True
    else:
        return False

@app.route('/upload', methods=['POST'])
def upload_page():
    print(PATHBASE)

    files = request.files.getlist('formFile')
    desiredExtension = request.form['fileType']

    folder_id=str(uuid.uuid1())
    files_list={}   # tuples list for starmap
    for f in files:
        if(check_extension(f, desiredExtension)):            
            id = str(uuid.uuid1())  # file id
            
            # add relevant values in files_list to pass in starmap
    
    
            # logger.info(f"Created file {id}")
            
    # create pool, call starmap,etc
    # pool.starmap(convert function, files_list)

    

    return redirect(f'/display', 303) 
    # user is directed to /display and using AJAX, converted files are displayed

@app.route('/display')
def display_page():
    """Display page to download files"""
    return render_template('display.html')

# @app.route('/status/<id>')
# def status_check(id):
#     """Return JSON with info about whether the uploaded file has been parsed successfully."""
#     if os.path.isdir(os.path.join(PATHBASE, 'uploads', id)):
#         for row in fileparsers.DATA:
#             if row['id']==id :
#                 stat, msg, err = row['status'], row['message'], bool(row['error_included'])
#                 break
#         return {'status':stat, 'message':msg, 'error_included':err}
#     else :
#         return '', 404

# def cleaner():
    
#     global app, PATHBASE
#     logger = logging.getLogger('fileclean')
#     logger.info('Cleaning up old files')
#     x=[]
#     for d in os.scandir(os.path.join(PATHBASE, 'uploads')):
#         if os.path.isdir(d):
#             try :
#                 shutil.rmtree(d, ignore_errors=True)
#                 x.append(d)
#             except :
#                 continue
#     logger.info("Removed"+str(x))
#     while True :
#         x = []
#         for i, (id, t) in enumerate(zip(fileparsers.DATA['id'], fileparsers.DATA['upload_time'])) :
#             if datetime.datetime.now() > t + fileparsers.UPLOAD_LIFETIME :
#                 try :
#                     shutil.rmtree(os.path.join(PATHBASE, 'uploads', id), ignore_errors=True)
#                     x.append(i)
#                     logger.info(f"Deleted {id}")
#                 except :
#                     logger.exception(f"Couldn't delete {id}")
#         fileparsers.DATA.remove_rows(x)
#         time.sleep(60 * 5)



if __name__ == '__main__':
    # _cleanerprocess = threading.Thread(target=cleaner)
    # _cleanerprocess.start()
    app.run(host='127.0.0.1', port=5000, debug=True)

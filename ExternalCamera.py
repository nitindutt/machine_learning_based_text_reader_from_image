__author__ = "Nitin Dutt"

import cv2
import datetime
import time
import os

VIDEO_INDEX = 0 #this is based on /ls/video<index  number on host machine>
class ExternalCamera(object):
    def opencv_take_screenshot(self, width = 1280, height = 1024):
        cam = cv2.VideoCapture(VIDEO_INDEX)
        cam.set(3, width)
        cam.set(4, height)
        cam.set(15, 0.1)
        cv2.namedWindow("test")

        ret, frame = cam.read()
        cv2.imshow("test", frame)

        if not ret:
            return False

        k = cv2.waitKey(3)

        date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        img_name = "opencv_frame_{}.png".format(date)
        cv2.imwrite(img_name, frame)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

        cv2.destroyAllWindows()
        cam.release()


    def opencv_take_video(self, min = .5, width = 1280, height = 1024):
        timeout = time.time() + 60*min

        cam = cv2.VideoCapture(VIDEO_INDEX)
        cam.set(3, width)
        cam.set(4, height)
        cam.set(15, 0.1)
        #for opencv 2.4.8
        #fourcc = cv2.cv.CV_FOURCC(*'XVID')
        #for opencv 3.4 and above

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        video_file_name = "opencv_video_{}.avi".format(date)

        # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (1280,1024))
        out = cv2.VideoWriter(video_file_name, fourcc, 20.0, (int(cam.get(3)), int(cam.get(4))))

        while (cam.isOpened()):
            ret, frame = cam.read()
            if ret == True:
                # frame = cv2.flip(frame, 0)
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & int(time.time()) > timeout:
                    break
            else:
                return False

        cam.release()
        out.release()
        cv2.destroyAllWindows()
        return video_file_name



    def FrameCaptureFromVideo(self, path): 
        # Path to video file
        vidObj = cv2.VideoCapture(path)
	  
        # Used as counter variable
        count = 0
        extractFramedir = os.path.join(os.getcwd(), datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
        os.makedirs(extractFramedir)
        # checks whether frames were extracted
        success = 1

        while success:
            # vidObj object calls read
            # function extract frames
            success, image = vidObj.read()

            # Saves the frames with frame-count
            cv2.imwrite(extractFramedir + "/" + "frame%d.jpg" % count, image)
            count += 1
  




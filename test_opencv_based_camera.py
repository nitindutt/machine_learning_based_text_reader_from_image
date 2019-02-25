import ExternalCamera


def main():
    camera = ExternalCamera.ExternalCamera()
    camera.opencv_take_screenshot()
    video_file = camera.opencv_take_video()
    print (video_file)
    camera.FrameCaptureFromVideo(video_file)



if __name__ == '__main__':
    main()

#
# marvin (c) by Jeffrey Maggio, Hunter Mellema, Joseph Bartelmo
#
# marvin is licensed under a
# Creative Commons Attribution-ShareAlike 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
#
#
import cv2
import imsciutils


class VideoWriter(object):
    """
    a wrapper class for the cv2 Video Writer:
    https://docs.opencv.org/3.0-beta/modules/videoio/doc/reading_and_writing_video.html#videowriter-fourcc

    This class will take a series of single frame imagery and
    """

    def __init__(self, filename="out_video.avi", fps=30.0, fourcc="XVID"):
        self.filename = imsciutils.util.prevent_overwrite(filename)
        self._fourcc = fourcc
        self._fourcc_val = cv2.VideoWriter_fourcc(*self._fourcc)
        self._fps = float(fps)
        self.__is_initialized = False

    def __init(self, size):
        """
        opens and initializes the videowriter
        """
        imsciutils.info("initializing the VideoWriter...")
        self._h, self._w = size
        self.video_writer_kwargs = {"filename": self.filename,
                                    "fourcc": self._fourcc_val,
                                    "fps": self._fps,
                                    "frameSize": (self._w, self._h)
                                    }
        self.writer = cv2.VideoWriter(**self.video_writer_kwargs)
        self.__is_initialized = True

    def write(self, frame):
        """
        writes a frame to the video file.
        automatically opens a video writer set to the input frame size
            frame: input frame to save to file
        return::
            None
        """
        if not self.__is_initialized:
            size = imsciutils.frame_size(frame)
            self.__init(size)

        if not self.writer.isOpened():
            self.writer.open(**self.video_writer_kwargs)

        self.writer.write(frame)

    def release(self):
        """
        closes the video writer
        input::
            None
        return::
            None
        """
        self.writer.release()

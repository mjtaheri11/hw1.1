import cv2


# if (cap.isOpened() == False):
#      print("Unable to read camera feed")

cap = cv2.VideoCapture(0)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter('outpy.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (frame_width, frame_height))
# while (True):
#     ret, frame = cap.read()
#     if ret == True:
#         out.write(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         else:
#             break
# cap.release()
# out.release()
# Closes all the frames
#cap = cv2.VideoCapture(0)

#
# while (True):
#     ret, frame = cap.read()
#     if ret == True:
#         out.write(frame)
#         cv2.imshow('frame', frame)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break
#         else:
#             break
# cap.release()
# cv2.destroyAllWindows()
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        out.write(frame)
        key = cv2.waitKey(27)
        if key == ord('q'):
            break
        # elif key == ord('s'):
        #     out.write(frame)
    else:
        break



cap.release()
#out.release()
cv2.destroyAllWindows()


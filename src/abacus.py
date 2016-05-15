import numpy as np
import cv2


cap = cv2.VideoCapture(1)


# Capture frame-by-frame
#ret, frame = cap.read()

# Our operations on the frame come here
#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# draw a rectangle
#cv2.rectangle(frame, (19, 27), (1279, 959), (0, 255, 0), 3)
#corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#corners = np.int0(corners)

        #for i in corners:
#    x, y = i.ravel()
#    cv2.circle(gray, (x, y), 3, 255, -1)
# Display the resulting frame
#cv2.imshow('frame',frame)
#if cv2.waitKey(1) & 0xFF == ord('q'):
#    break

# height, width, depth = frame.shape
# #blue dot rgb value: 124, 182, 239
# for i in range(0, height):
#     for j in range(0, width):
#         if frame[i, j][0] > 200 and frame[i,j][1]<200 and frame[i,j][2]<200 and frame[i, j][0] < 250 and frame[i,j][1]>150 and frame[i,j][2]>100:
#             #print frame[i,j]
#             print "x = " + str(i)
#             print "y = " + str(j)
#             print "========="


while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # This is the main rectangle frame.
    #cv2.rectangle(frame, (35, 50), (1200,550), (0, 255, 0), 3)
    #cv2.rectangle(frame, (90, 80), (1150, 500), (0, 255, 0), 3)
    width =  (1150 - 90)/13
    height = 500 - 80
    cv2.line(gray, (90,350), (1142,350), (0,255,0), 3)

    # Vertical line going downwards (bead measurement line)
    cv2.line(gray,(130,80),(130,115),(0,255,0), 3)

    # 27,27,27 - bead color (black)
    # 127,127,127 - metal rod (gray)
    # 165, 165, 165 - stick (grayish)

    # (x-coord, y-coord)
    # (x-coord_col, 80 + 35*j + 35/2) (x-coord_col + bead length,  80 + 35*j + 35/2)


    bead = 40
    bottom_frame = 490

    # These are the columns of the abacus
    # cv2.rectangle(frame, (90, 80), (90+width, 500),(0, 255, 0), 3)
    for i in range(0,1): # Traditionally 13
        cv2.rectangle(gray, (90 + i*width, 80), (90 + (i+1)*width, bottom_frame), (0, 255, 0), 3)
        for j in range(0,1): # Traditionally 5
            gray_sum = 0
            x_min = 90 + i*width
            x_max = 90 + (i+1)*width
            y = 80+bead*j + (bead/2)
            for k in range(x_min, x_max):
                if k > 959:
                    break
                gray_sum += gray[k, y]
            gray_avg = gray_sum / (x_max - x_min)
            print gray_avg
            cv2.line(gray, (x_min, y), (x_max, y), (0,255,0), 3)
        for j in range(0,2):
            cv2.line(gray, (90 + i*width, bottom_frame - 80+bead*j + (bead/2)), (90 + (i+1)*width, bottom_frame - 80+bead*j + (bead/2)), (0,255,0), 3)

    print("done")

    #corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    #corners = np.int0(corners)

            #for i in corners:
    #    x, y = i.ravel()
    #    cv2.circle(gray, (x, y), 3, 255, -1)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break

    # height, width, depth = frame.shape
    # #blue dot rgb value: 124, 182, 239
    # for i in range(0, height):
    #     for j in range(0, width):
    #         if frame[i, j][0] > 200 and frame[i,j][1]<200 and frame[i,j][2]<200 and frame[i, j][0] < 250 and frame[i,j][1]>150 and frame[i,j][2]>100:
    #             #print frame[i,j]
    #             print "x = " + str(i)
    #             print "y = " + str(j)
    #             print "========="



# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


import numpy as np
import cv2
import pusher

pusher_client = pusher.Pusher(
  app_id='209391',
  key='3a07e26ad5dafe9ae4ca',
  secret='cc88a22eaeea4ed58b9a',
  ssl=True
)

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
    #Find Sum
    # sum = 0
    # for i in range(0, 13):
    #     sum += 15 * (10**i)
    # print sum

    sum = 16666666666665

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # This is the main rectangle frame.
    cv2.rectangle(frame, (35, 50), (1200,550), (255, 255, 255), 3)
    cv2.rectangle(frame, (90, 80), (1150, 500), (255, 255, 255), 3)
    width =  (1150 - 90)/13
    height = 500 - 80
    # cv2.line(gray, (90,350), (1142,350), (0,255,0), 3)

    # Vertical line going downwards (bead measurement line)
    # cv2.line(gray,(130,80),(130,115),(0,255,0), 3)

    # 27,27,27 - bead color (black)
    # 127,127,127 - metal rod (gray)
    # 165, 165, 165 - stick (grayish)

    # (x-coord, y-coord)
    # (x-coord_col, 80 + 35*j + 35/2) (x-coord_col + bead length,  80 + 35*j + 35/2)


    bead_color_threshold = 70

    bead = 40
    bottom_frame = 490

    column_array = []
    num_beads = 0
    # These are the columns of the abacus
    # cv2.rectangle(frame, (90, 80), (90+width, 500),(0, 255, 0), 3)

    num_col = 0
    # COLUMNS
    for i in range(0,13): # Traditionally 13
        num_beads = 0
        num_col+=1
        cv2.rectangle(gray, (90 + i*width, 80), (90 + (i+1)*width, bottom_frame), (255, 255, 255), 3)

        #ROWS
        for j in range(0,5): # Traditionally 5
            gray_sum = 0
            x_min = 90 + i*width
            x_max = 90 + (i+1)*width
            #print "x_min = " + str(x_min)
            #print "x_max = " + str(x_max)
            y = 80+bead*j + (bead/2)

            #EACH BEAD
            for k in range(x_min, x_max):
                # if k > 959 and i > 10:
                #     break
                gray_sum += gray[y, k]
            gray_avg = gray_sum / (x_max - x_min)
            #print "Gray avg of col " + str(i) + " row "+ str(j) +"="+str(gray_avg)
            if gray_avg <= bead_color_threshold:
                num_beads+=1
                sum -= 10 ** i
            else:
                break

            # print gray_avg
            cv2.line(gray, (x_min, y), (x_max, y), (255,255,255), 3)
        column_array.append(num_beads)
        #print "Number of beads in col " + str(num_col) + ": " + str(num_beads)
        for j in range(0,2):
            gray_sum = 0
            x_min = 90 + i * width
            x_max = 90 + (i + 1) * width
            # print "x_min = " + str(x_min)
            # print "x_max = " + str(x_max)
            y = bottom_frame - 80 + bead * (1-j) + (bead / 2)

            # EACH BEAD
            for k in range(x_min, x_max):
                # if k > 959 and i > 10:
                #     break
                gray_sum += gray[y, k]
            gray_avg = gray_sum / (x_max - x_min)
            # print "Gray avg of col " + str(i) + " row "+ str(j) +"="+str(gray_avg)
            if gray_avg <= bead_color_threshold:
                sum -= 5 * (10 ** i)
                num_beads += 1
            else:
                break
            cv2.line(gray, (90 + i*width, bottom_frame - 80+bead*(1-j) + (bead/2)), (90 + (i+1)*width, bottom_frame - 80+bead*(1-j) + (bead/2)), (255,255,255), 3)

    final_sum = sum
    pusher_client.trigger('abacus_channel', 'updated', final_sum)
    print final_sum
    #print("done")

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


img = imread("C:\Users\avdhe\Downloads\img_51.jpg"); % Input the image file 

theta = 51; % angle by which image is to be rotated
rmat = [ cos(theta) sin(theta) 0
-              sin(theta) cos(theta) 0
               0 0 1]; % defining rotation matrix

mx = size(img,2); % number of rows
my = size(img,1); % number of columns

corners = [ 0 0 1
                   mx 0 1
                   0 my 1
                   mx my 1]; % defining corner matrix

new_c = corners*rmat; % rotating the image

T = maketform('affine', rmat);   % translation line

img2 = imtransform(img, T, ...
    'XData',[min(new_c(:,1)) max(new_c(:,1))],...
    'YData',[min(new_c(:,2)) max(new_c(:,2))]); % final rotated image

figure;
imshow(img);
title('Original Image U19ME191');

figure;
imshow(img2);
title('Rotated image by 51   degrees U19ME191');

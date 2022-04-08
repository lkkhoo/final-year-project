clc;
clear all;
close all;
I=imread('lfsr1.png');
A=double(I);
%%%% Horizontal %%%%
x1 = double(A(:,1:end-1));
y1 = double(A(:,2:end));
randIndex1 = randperm(numel(x1));
randIndex1 = randIndex1(1:3000);
x11 = x1(randIndex1);
y11 = y1(randIndex1);
%%% Vertical %%%%%
x2 = double(A(1:end-1,:));
y2 = double(A(2:end,:));
randIndex1 = randperm(numel(x2));
randIndex1 = randIndex1(1:3000);
x21 = x2(randIndex1);
y21 = y2(randIndex1);
%%%% Diagonal %%%%%
x3 = double(A(1:end-1,1:end-1));
y3 = double(A(2:end,2:end));
randIndex1 = randperm(numel(x3));
randIndex1 = randIndex1(1:3000);
x31 = x3(randIndex1);
y31 = y3(randIndex1);
r_xy1 = corrcoef(x11,y11)
r_xy2 = corrcoef(x21,y21)
r_xy3 = corrcoef(x31,y31)
figure,
subplot(1,3,1)
scatter(x11,y11);
subplot(1,3,2)
scatter(x21,y21);
subplot(1,3,3)
scatter(x31,y31);

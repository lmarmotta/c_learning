clear all
close all

% INPUT: Define the number of points in the grid.
n_points = 100;

grid = linspace(-5,5,n_points);

% Create the property verctors.
Q = zeros(3,n_points);
F = zeros(3,n_points);


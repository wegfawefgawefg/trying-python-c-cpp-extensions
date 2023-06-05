cmake_minimum_required(VERSION 3.0)
project(my_project)

# Specify the C standard
set(CMAKE_C_STANDARD 11)
set(CMAKE_C_STANDARD_REQUIRED True)

# Add fibonacci library
add_library(fibonacci SHARED src/fibonacci.c)

# Add vec library
add_library(vec SHARED src/vec.c)

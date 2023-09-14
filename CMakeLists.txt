cmake_minimum_required(VERSION 3.0)
project(SDL2_mixer)

find_package(SDL2 REQUIRED)
find_package(SDL2_mixer REQUIRED)

add_executable(your_executable_name audio.c)

target_link_libraries(your_executable_name SDL2::SDL2 SDL2::Mixer)

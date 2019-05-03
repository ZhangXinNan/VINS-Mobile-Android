cmake_minimum_required(VERSION 3.4.1)
project(VINSMobile)

set(boost_include_dir /Users/zhangxin/tools/boost/boost_1_63_0)

# done here so it's not necessary for every target_link_library call of opencv
# SET(OpenCV_DIR {path}/OpenCV-android-sdk/sdk/native/jni)
SET(OpenCV_DIR /Users/zhangxin/tools/opencv4android/4.1.0/OpenCV-android-sdk/sdk/native/jni)
find_package(OpenCV REQUIRED)

# this is branching into all the subdirectories and thus connecting them all
add_subdirectory(VINS_ThirdPartyLib)
add_subdirectory(ThirdParty/DBoW)
add_subdirectory(ThirdParty/DUtils)
add_subdirectory(ThirdParty/DVision)
add_subdirectory(VINS_ios)
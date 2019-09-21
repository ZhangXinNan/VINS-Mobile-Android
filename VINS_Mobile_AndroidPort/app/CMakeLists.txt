# For more information about using CMake with Android Studio, read the
# documentation: https://d.android.com/studio/projects/add-native-code.html

# Sets the minimum version of CMake required to build the native library.

cmake_minimum_required(VERSION 3.4.1)


# cmake opencv config
SET(OpenCV_DIR /home/zhangxin/tools/opencv4android/4.1.0/OpenCV-android-sdk/sdk/native/jni)

set(OPENCV_INCLUDE_DIR /home/zhangxin/tools/opencv4android/4.1.0/OpenCV-android-sdk/sdk/native)
#include_directories(${OPENCV_INCLUDE_DIR}/jni/include)
set(OPENCV_LIB_DIR /home/zhangxin/tools/opencv4android/4.1.0/OpenCV-android-sdk/sdk/native/libs)
##静态方式加载
#add_library( lib_opencv_calib3d STATIC IMPORTED )
#set_target_properties(lib_opencv_calib3d PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_calib3d.a)
#
#add_library( lib_opencv_core STATIC IMPORTED )
#set_target_properties(lib_opencv_core PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_core.a)
#
#add_library( lib_opencv_features2d STATIC IMPORTED )
#set_target_properties(lib_opencv_features2d PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_features2d.a)
#
#add_library( lib_opencv_flann STATIC IMPORTED )
#set_target_properties(lib_opencv_flann PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_flann.a)
#
#add_library( lib_opencv_highgui STATIC IMPORTED )
#set_target_properties(lib_opencv_highgui PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_highgui.a)
#
#add_library( lib_opencv_imgcodecs STATIC IMPORTED )
#set_target_properties(lib_opencv_imgcodecs PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_imgcodecs.a)
#
#add_library( lib_opencv_imgproc STATIC IMPORTED )
#set_target_properties(lib_opencv_imgproc PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_imgproc.a)
#
#add_library( lib_opencv_ml STATIC IMPORTED )
#set_target_properties(lib_opencv_ml PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_ml.a)
#
#add_library( lib_opencv_objdetect STATIC IMPORTED )
#set_target_properties(lib_opencv_objdetect PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_objdetect.a)
#
#add_library( lib_opencv_photo STATIC IMPORTED )
#set_target_properties(lib_opencv_photo PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_photo.a)
#
#add_library( lib_opencv_shape STATIC IMPORTED )
#set_target_properties(lib_opencv_shape PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_shape.a)
#
#add_library( lib_opencv_stitching STATIC IMPORTED )
#set_target_properties(lib_opencv_stitching PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_stitching.a)
#
#add_library( lib_opencv_superres STATIC IMPORTED )
#set_target_properties(lib_opencv_superres PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_superres.a)
##
##add_library( lib_opencv_ts STATIC IMPORTED )
##set_target_properties(lib_opencv_ts PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_ts.a)
#
#add_library( lib_opencv_video STATIC IMPORTED )
#set_target_properties(lib_opencv_video PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_video.a)
#
#add_library( lib_opencv_videoio STATIC IMPORTED )
#set_target_properties(lib_opencv_videoio PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_videoio.a)
#
#add_library( lib_opencv_videostab STATIC IMPORTED )
#set_target_properties(lib_opencv_videostab PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_videostab.a)

add_library( opencv SHARED IMPORTED )
set_target_properties(opencv PROPERTIES IMPORTED_LOCATION ${OPENCV_LIB_DIR}/${ANDROID_ABI}/libopencv_java4.so)

set(LIB_NAME NativeLib)
set(
    ${LIB_NAME}_SRCS
    src/main/cpp/jni/nativelib.cpp
)


add_subdirectory(libs/VINS-Mobile-master)

add_subdirectory(src/main/cpp/VINS_Android)


# Gradle automatically packages shared libraries with your APK.
add_library( 
    ${LIB_NAME}
    SHARED
    ${${LIB_NAME}_SRCS}
)

# Searches for a specified prebuilt library and stores the path as a
# variable. Because CMake includes system libraries in the search path by
# default, you only need to specify the name of the public NDK library
# you want to add. CMake verifies that the library exists before
# completing its build.

find_library( 
    # Sets the name of the path variable.
    log-lib
    
    # Specifies the name of the NDK library that
    # you want CMake to locate.
    log 
)

#add_dependencies(nativelib VINS_Android)

# Specifies libraries CMake should link to your target library. You
# can link multiple libraries, such as libraries you define in this
# build script, prebuilt third-party libraries, or system libraries.

target_link_libraries( 
    # Specifies the target library.
    NativeLib
    opencv
#    lib_opencv_calib3d
#    lib_opencv_core
#    lib_opencv_features2d
#    lib_opencv_flann
#    lib_opencv_highgui
#    lib_opencv_imgcodecs
#    lib_opencv_imgproc
#    lib_opencv_ml
#    lib_opencv_objdetect
#    lib_opencv_photo
#    lib_opencv_shape
#    lib_opencv_stitching
#    lib_opencv_superres
##    lib_opencv_ts
#    lib_opencv_video
#    lib_opencv_videoio
#    lib_opencv_videostab
    # VINSMobile
    
    VINS_Android
    
    log
    # Links the target library to the log library
    # included in the NDK.
    #${log-lib}
)
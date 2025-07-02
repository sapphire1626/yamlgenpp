if(NOT TARGET yaml-cpp::yaml-cpp)
    find_package(yaml-cpp QUIET)
    if(NOT TARGET yaml-cpp::yaml-cpp)
        include(FetchContent)
        FetchContent_Declare(
          yaml-cpp
          GIT_REPOSITORY https://github.com/jbeder/yaml-cpp.git
          GIT_TAG 0.8.0
        )
        FetchContent_MakeAvailable(yaml-cpp)
    endif()
endif()

if(EXISTS ${CMAKE_CURRENT_LIST_DIR}/yamlgenpp/main.py)
    set(YAMLGENPP_COMMAND python3 ${CMAKE_CURRENT_LIST_DIR}/yamlgenpp/main.py)
else()
    find_program(YAMLGENPP_COMMAND yamlgenpp)
endif()

function(add_yamlgenpp_target TARGET)
    set(CPP_SOURCES )
    foreach(SOURCE ${ARGN})
        get_filename_component(SOURCE_NAME ${SOURCE} NAME_WE)
        list(APPEND CPP_SOURCES
            ${CMAKE_CURRENT_BINARY_DIR}/yamlgenpp/${SOURCE_NAME}.cpp
            ${CMAKE_CURRENT_BINARY_DIR}/yamlgenpp/${SOURCE_NAME}.hpp
        )
    endforeach()
    add_custom_command(
        OUTPUT ${CPP_SOURCES}
        COMMAND ${YAMLGENPP_COMMAND} ${ARGN} -d ${CMAKE_CURRENT_BINARY_DIR}/yamlgenpp
        DEPENDS ${ARGN}
        COMMENT "Generating yamlgenpp struct"
    )
    add_library(${TARGET} OBJECT ${CPP_SOURCES})
    target_include_directories(${TARGET} PUBLIC ${CMAKE_CURRENT_BINARY_DIR}/yamlgenpp)
    target_link_libraries(${TARGET} PUBLIC yaml-cpp::yaml-cpp)
endfunction()

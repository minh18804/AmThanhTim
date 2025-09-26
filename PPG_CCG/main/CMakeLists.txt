idf_component_register(SRCS "main.c"
                    INCLUDE_DIRS "." "../component/MAX30102" "../component/i2cdev" "../component/FileManager"
                    REQUIRES    esp_driver_i2s    driver)

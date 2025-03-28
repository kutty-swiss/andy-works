#!/bin/bash

# Set up Intel oneAPI environment
source /opt/intel/oneapi/setvars.sh

# Set compilers for SYCL
export CMAKE_C_COMPILER=icx
export CMAKE_CXX_COMPILER=icpx

# Set oneDNN (DNNL) path if needed
export DNNL_DIR=/opt/intel/oneapi/dnnl/latest
export TBB_DIR=/opt/intel/oneapi/tbb/latest
export CMAKE_PREFIX_PATH=$DNNL_DIR:$CMAKE_PREFIX_PATH

# Clone the stable-diffusion.cpp repository if it doesn't exist
if [ ! -d "~/stable-diffusion.cpp" ]; then
    echo "Cloning stable-diffusion.cpp repository..."
    git clone https://github.com/leejet/stable-diffusion.cpp.git ~/stable-diffusion.cpp
else
    echo "Repository already exists. Pulling the latest changes..."
    cd ~/stable-diffusion.cpp
    git pull origin main
fi

# Go to the project directory
cd ~/stable-diffusion.cpp

# Initialize and update submodules
git submodule init
git submodule update

# Create build directory if it doesn't exist
mkdir -p build
cd build

# Run CMake configuration with SYCL, Vulkan, and OpenBLAS support
cmake .. -DSD_SYCL=ON -DSD_VULKAN=ON -DGGML_OPENBLAS=ON -DCMAKE_C_COMPILER=icx -DCMAKE_CXX_COMPILER=icpx  -DINTEL_MKL_DIR=/opt/intel/oneapi/mkl/latest -DTBB_DIR=/opt/intel/oneapi/tbb/latest


# Build the project using all available CPU cores
cmake --build . --config Release -j$(nproc)

echo "Build completed successfully!"

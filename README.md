## Steps to Set up
1. Activate conda env with the infEngine.yml file
2. install the cuda toolkit - 12.6
3. Install sglang using this guide: https://docs.sglang.ai/get_started/install.html
4. Install hugging face cli: https://huggingface.co/docs/huggingface_hub/en/guides/cli and login
5. `export LD_LIBRARY_PATH=/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH` in case it can't find gcc
## Debugging
1. In case nvcc still says command not known
    - `export PATH=/usr/local/cuda-12.6/bin:$PATH`
    - `export LD_LIBRARY_PATH=/usr/local/cuda-12.6/lib64:$LD_LIBRARY_PATH`
2. Triton tries to look for libcuda.so but there is a file called `libcuda.so.1`. Just simlink it to libcuda.so like below:
    - `sudo ln -s /usr/lib/x86_64-linux-gnu/libcuda.so.1 /usr/lib/x86_64-linux-gnu/libcuda.so`


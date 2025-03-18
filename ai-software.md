# AI Tools and Software for Linux

## **1. LLM Models and Interfaces**  
These tools help run and interact with large language models locally, giving you the flexibility to work with powerful AI models without relying on cloud services.

- **[llama.cpp](https://github.com/ggerganov/llama.cpp)**  
  A lightweight, high-performance implementation of LLaMA models, designed to run efficiently on local hardware.

   <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Llama1-logo.png/220px-Llama1-logo.png" width="400" height="150">  

- **[Ollama](https://ollama.com)**  
  Provides easy-to-use local inference for large language models with a focus on simplicity and performance.

  <img src="https://www.linuxtricks.fr/upload/ollama-logo.png" width="400" height="150">  

- **[Open-WebUI](https://github.com/Open-WebUI/Open-WebUI)**  
- Open-WebUI** is a simple, extensible, and easy-to-use interface for running **LLM inference**. It provides a clean and intuitive web interface to manage models and their configurations.  
- **Key Features**:  
  - Easy installation and setup of **local LLMs**  
  - Configurable model settings and parameters  
  - Extensible plugins and support for various AI models  
  - Real-time monitoring and control over AI workflows  
  - Ideal For: Users who prefer a **web-based UI** for managing AI inference tasks locally, with a focus on simplicity and expandability.  

<img src="https://openwebui.com/favicon.png" width="200" height="200">
---

- **[GPT4All](https://github.com/nomic-ai/gpt4all)**  
  A community-driven project providing a collection of LLMs, particularly optimized for running on local hardware.

  <img src="https://www.nomic.ai/gpt4all/gpt4all_word.svg" width="200" height="200">  

- **[Jan](https://github.com/jan-code/jan)**  
  A local framework to run, manage, and interact with multiple language models, simplifying model deployment and inference.

  <img src="https://images.glints.com/unsafe/160x0/glints-dashboard.oss-ap-southeast-1.aliyuncs.com/company-logo/ff2621a5ee466860f87de7b5d1fc5a7d.png" width="200" height="200">  

## **2. AI File Management & Utilities**  
These tools help manage and utilize AI-generated files, enhance workflows, and improve model efficiency.

- **[LM Studio](https://lmstudio.ai/)**  
- Best Pick for AI Inference**: LM Studio is my go-to choice for **LLM inference** as it provides the easiest way to **download and run** large language models.  
- Efficient Resource Management**: After some learning, I figured out how to split the load between **CPU and GPU** using Vulkan, enhancing performance.  
- Favorite Feature - RAG**: LM Studio also integrates **RAG (Retrieval-Augmented Generation)**, making it incredibly useful for AI-based tasks.

<img src="https://lmstudio.ai/_next/static/media/lmstudio-app-logo.61cb7d80.webp" alt="LM Studio Logo" width="200" height="200">  
 
- **[Lamafile](https://github.com/lamafile/lamafile)**  
  An AI-optimized single cross platform file and management tool from mozilla, that streamlines the process of managing AI models and outputs.

  <img src="https://github.com/Mozilla-Ocho/llamafile/raw/main/llamafile/llamafile-640x640.png" width="200" height="200">  

- **[PyGPT](https://github.com/pytorch/pytorch)**  
  A lightweight implementation of GPT models in Python, allowing quick deployment and testing on local systems.

  <img src="https://pygpt.net/assets/logo_pygpt_v2.png?v=20240218" width="300" height="200">  

- **[Local AI](https://localai.com)**  
  A platform for running AI models locally, allowing users to perform inference without relying on external cloud services.  
  Specialty is it allows different types of AI models like text to chat, text to image, text to voice, voice to etc etc.

  <img src="https://github.com/go-skynet/LocalAI/assets/2420543/0966aa2a-166e-4f99-a3e5-6c915fc997dd" width="200" height="200">  

## **3. Image Generation & AI Art**  
AI tools focused on generating images, enhancing them, and applying diffusion models to create or upscale content.

- **[Easy Diffusion](https://github.com/easydiffusion/easydiffusion)**  
  An AI tool for generating images from text prompts using diffusion models. Great for artists and creatives.

  <img src="https://stable-diffusion.hexaltation.org/media/images/icon-512x512.png" width="200" height="200">  

- **[Auto1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui)**  
  A popular web UI for running Stable Diffusion, allowing easy integration with various image generation models.

  <img src="https://user-images.githubusercontent.com/36368048/196056944-6e8f039f-1a81-4d8b-b513-b49b1edef1ce.png" width="200" height="200">  

- **[Forge](https://github.com/forge/forge)**  
  A tool to quickly generate and refine AI art using advanced diffusion techniques and customizable settings.

- **[Reforge](https://github.com/reforge/reforge)**  
  Another image generation tool optimized for creative outputs and flexible image modification based on AI models.

- **[ComfyUI](https://github.com/comfyui/comfyui)**  
  A user-friendly interface for AI-generated art, combining a simple UI with powerful features for generating and editing images.

  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTgYeNeytLVoTAwPQyXHiLmlv9tDg46J3HhbQ&s" width="200" height="200">  

- **[Upscayl](https://github.com/upscayl/upscayl)**  
  An AI-powered image upscaling tool that improves the quality of images without losing details or introducing noise.

  <img src="https://dashboard.snapcraft.io/site_media/appmedia/2023/04/upscayl.png" width="200" height="200">  

## **4. AI Development Platforms**  
Tools for running and experimenting with AI models, typically for developers looking to integrate or build upon existing AI frameworks.

- **[Intel AI Playground (Windows)](https://www.intel.com/content/www/us/en/artificial-intelligence/ai-playground.html)**  
  A Windows-based platform from Intel designed for experimenting with various AI models, optimized for Intel hardware.

    <img src="https://cdn.mos.cms.futurecdn.net/d8pmQi6W7Vfvp2w2EhkAtG-650-80.png.webp" width="400" height="200">  

## **5. Key learnings**
  Large language models consume lot of space. So i decided to have them in a common shared folder. Based on the tool type, i had to set the parameters in yaml files, export system variables or create symlinks.

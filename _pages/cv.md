---
layout: archive
title: "Kaiming Fu"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---
<!-- You can download a PDF copy of my resume [here](../files/KaimingFu_Resume.pdf).-->

Education
-----
* Ph.D. in Electrical and Computer Engineering, University of California, Davis, 2024 (expected)
* Double-Major M.S. in Statistic, University of California, Davis, 2022
* M.S. in Mechanical Engineering, Purdue University, West Lafayette, 2019

Research experience
-----
* Crop Counting Through Deep Learning Enhanced By Synthetic Images
  * Created a dataset of RGB and NIR walnut images, manually annotated, and sourced from a multispectral camera.
  * Enhanced walnut detection algorithms by generating synthetic images (RGB and NIR) with the based on radiation model in Helios, using reverse ray-tracing to accurately label walnuts.
  * Utilized YOLOv5 on the augmented datasets, achieving detection accuracy improvements of 11.4% in RGB  images and 18.9% in NIR images.

* Integrated 2D and 3D Fruit Mapping for Optimized Harvesting Simulation and Planning
  * Analyzed 3D fruit distribution using a fusion of sensors (IMU, LiDAR, thermal camera) combined with SLAM techniques for precise localization of harvestable areas, facilitating GPS-independent harvesting planning.
  * Unified high-resolution LiDAR data and radiative ray tracing methods to reconstruct detailed tree models, overlaying both actual and synthetic fruit distributions for comprehensive 2D and 3D mapping.
  * Merged comprehensive datasets capturing fruit distribution through sensor fusion with detailed tree architecture from high-resolution LiDAR, enhancing neural network training for the generation of precise synthetic fruit distribution models.

* Simulation Design and Optimization of Agricultural Robotics
  * Established a comprehensive robot-tree-fruit simulation environment by creating precise digital models to accurately represent real-world agricultural scenarios.
  * Conducted an interference study using voxel-based modeling accelerated by CUDA, enabling the evaluation and enhancement of harvester design through fruit collection efficiency metrics.
  * Optimized a dynamic planning algorithm that leverages visible fruit distribution data, obtained from in-field computer vision systems, to inform and refine the robotic harvesting strategy.


Projects
-----
* Annual Farm Robotics Challenge
  * Team Leader. Grand Prize Winner among National-wide Universities and Colleges
    * Designed a DepthAI-based real-time monitor system within a harvesting assistant robot, capable of autonomously tracking human operators and providing immediate posture analysis feedback, enhancing worker safety and efficiency through a custom Human Monitoring System.
    * Optimized agricultural productivity by enabling the robot to transport harvested crops directly to storage, effectively eliminating the reliance on manual tractor transportation.

* ”Inceptio-Tsinghua AIR Cup” Autonomous Driving Challenge
  * 1st Prize Winner among 1067 Teams
    * Utilized an Xbox controller to collect driving data for training a neural network with Imitative Learning, collaborating on semi-trailer acceleration control with the LCA lane keeping system.
    * Employed a range of advanced problem-solving techniques, including two-way search, greedy algorithms, space pruning, convex optimization, and the deep reinforcement learning PPO algorithm.

* Fine-Grained Classification in Plant Pathology
  * IEEE / CVF Computer Vision and Pattern Recognition Conference (CVPR) workshop
    * Preprocessed imbalanced dataset using a data sampler, employed ResNet50 as the baseline, achieving an F1 score of 0.70.
    * Implemented a Generative Data Augmentation model for image augmentation and training dataset balance.
    * Improved F1 score to 0.874 using a UNet-ResNet generator and a DenseNet discriminator.

Skills
-----
* Programming Languages: C++, Python, R, Matlab.
* Tools:
  * CUDA
  * Pytorch
  * Scikit-Learn
  * TensorFlow
  * Neural Networks (YOLO, CNN, Fast RCNN, Faster RCNN, ResNet)


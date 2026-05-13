## Unity-MediaPipe Real-Time Hand Telemetry Integration

This repository showcases a high-performance integration between **Python-based computer vision** and the **Unity 6 Engine**. The project establishes a low-latency data pipeline to stream 3D hand landmark coordinates for real-time skeletal reconstruction and environment interaction.

---
<center><img width="937" height="474" alt="Screenshot 2026-05-12 222228" src="https://github.com/user-attachments/assets/4e64f7b2-0911-4f8e-bddc-5793b03b8d4c" /><center/>
---

### ## Technical Architecture

The project architecture facilitates a decoupled processing loop to maintain high frame rates in both the vision and rendering threads:

* **Vision Subsystem (Python):**
* Utilizes `MediaPipe` for GPU-accelerated hand landmark detection.
* Processes 21 key points per hand using `cv2` and `cvzone` for spatial coordinate extraction.
* Labels hand chirality (Left/Right) dynamically based on landmark orientation.


* **Communication Layer:**
* Broadcasts serialized coordinate strings (e.g., `[x, y, z]` arrays) from the Python environment to Unity.


* **Rendering & Logic (Unity/C#):**
* Built on **Unity 6 (6000.0.0f1)** using the **Universal Render Pipeline (URP)** for optimized lighting and shader support.
* A C# controller parses incoming telemetry data to update the Transform positions of 21 tracked GameObjects in real-time.
* Dynamic skeletal rendering is achieved via **Line Renderers** that connect the joint nodes into a coherent hierarchical structure.



---

### ## Project Components

* **Hand Skeletonization:** Implemented via a `linecode` script that manages the vertex positions of Line Renderers to visualize the hand’s topology.
* **Asset Management:** Uses a modular hierarchy featuring a `manager` object to handle data ingestion and a `hands` parent object containing individual joint spheres.
* **Testing Environment:** A prototyping scene utilizing **Gridbox Prototype Materials** for spatial calibration and depth testing.

---

### ## Technical Highlights

* **Real-Time Data Parsing:** Demonstrates efficient handling of high-frequency data streams (as seen in the console logs) to drive 3D physics-enabled objects.
* **Coordinate Mapping:** Transposes 2D/3D camera-space coordinates from MediaPipe into Unity’s world-space coordinates with minimal latency.
* **Shader Integration:** Leveraging URP shaders to provide consistent visual feedback across both the game scene and the hand representation.

---
<img width="937" height="474" alt="Screenshot 2026-05-13 060558" src="https://github.com/user-attachments/assets/c1b4aab3-37e9-4e00-a167-323c9e44ed39" />
<img width="937" height="474" alt="Screenshot 2026-05-12 222419" src="https://github.com/user-attachments/assets/e5e0f418-dc72-495d-8111-e60e2930c8bf" />
<img width="937" height="474" alt="Screenshot 2026-05-12 222228" src="https://github.com/user-attachments/assets/4e64f7b2-0911-4f8e-bddc-5793b03b8d4c" />


> **Note:** This is a showcase project highlighting the technical feasibility of cross-platform telemetry and real-time computer vision integration within a modern game engine.

import glfw
from OpenGL.GL import *
from OpenGL.GL import shaders
import numpy as np

# GLFW setup
glfw.init()

glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)  # APPLE ONLY

# Create and focus GLFW window
window = glfw.create_window(800, 600, "Robot Interface", None, None)
glfw.make_context_current(window)

# Placeholder Triangle Geometry
# TODO: Allow .obj imports
geometry = np.array([
    -0.5, -0.5, 0.0,
    0.5, -0.5, 0.0,
    0.0, 0.5, 0.5
], dtype=np.float32)

# Translating raw data into VAO and VBO objects
vao = glGenVertexArrays(1)
glBindVertexArray(vao)

vbo = glGenBuffers(1)
glBindBuffer(GL_ARRAY_BUFFER, vbo)
glBufferData(GL_ARRAY_BUFFER, geometry.nbytes, geometry, GL_STATIC_DRAW)

# Shader values
# TODO: Figure out how to use glGetAttribLocation for these values
glEnableVertexAttribArray(0)  # 0 = Position attribute
glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)  # No clue what this does, but it makes the shaders work

# Pull source from glsl shader files
with open('./interface/shader.vert', 'r') as f:
    vertexShader = shaders.compileShader(f.read(), GL_VERTEX_SHADER)
with open('./interface/shader.frag', 'r') as f:
    fragmentShader = shaders.compileShader(f.read(), GL_FRAGMENT_SHADER)

# Compile shaders from source
shaderProgram = shaders.compileProgram(vertexShader, fragmentShader)


while not glfw.window_should_close(window):
    glClearColor(0, 0, 0, 1)  # Black background
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glUseProgram(shaderProgram)  # Execute Shaders
    glDrawArrays(GL_TRIANGLES, 0, 3)  # Draw geometry (replace with drawElements)
    glUseProgram(0)  # Unset shader program

    glfw.swap_buffers(window)
    glfw.poll_events()  # Waits for next frame

glfw.terminate()

#version 400 core

in vec4 position;
out vec3 color;

void main () {

    gl_Position = position;
    color = vec3(position.x + 0.5, 1.0, position.y + 0.5);

}
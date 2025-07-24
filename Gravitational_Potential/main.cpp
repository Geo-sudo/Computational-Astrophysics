#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include <iostream>
#include <vector>
#include <cmath>


class Body {
public:
    float pos_X,pos_Y,pos_Z=0;
    float vel_X,vel_Y,vel_Z=0;
    float radius;
    int segments;
    std::vector<float> vertices;

    Body(float x_, float y_, /*float z_,*/ float vel_x_, float vel_y_, /*float vel_z_,*/ float radius_, int segments_){
        pos_X=x_; pos_Y=y_; /*pos_Z=z_;*/ vel_X=vel_x_; vel_Y=vel_y_; /*vel_Z=vel_z_;*/ radius=radius_; segments = segments_;
        vertices = genCircle(segments);
    }

    std::vector<float> genCircle(int segments){
    std::vector<float> vertices;
    vertices.push_back(0.0f);
    vertices.push_back(0.0f);
    vertices.push_back(0.0f);
    for(int i=0; i <= segments; i++){
        float angle = 2.0f * M_PI * float(i)/float(segments);
        vertices.push_back(cosf(angle)); 
        vertices.push_back(sinf(angle));
        vertices.push_back(0.0f);
    }
    
    return vertices;
    }

    void update_parameters(float dt){
        pos_X += vel_X * dt;
        pos_Y += vel_Y * dt;
        if (pos_X + radius > 1.0f || pos_X - radius < -1.0f) {vel_X = -vel_X;}
        if (pos_Y + radius > 1.0f || pos_Y - radius < -1.0f) {vel_Y = -vel_Y;}
    }

    void render(GLuint shaderProgram){
        GLint radiusLoc = glGetUniformLocation(shaderProgram, "radius");
        GLint offsetLoc = glGetUniformLocation(shaderProgram, "offset");
        glUniform2f(offsetLoc, pos_X, pos_Y);
        glUniform1f(radiusLoc, radius);
    }

};

int main() {

    auto UnitCircle = Body(0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 100);
    auto object1 = Body(0.0f, 0.5f, 1.3f, 2.1f, 0.2f, 100);
    auto object2 = Body(0.3f, -0.2f, 1.0f, -1.5f, 0.1f, 100);
    std::vector<Body> objects;
    objects.emplace_back(object1);
    objects.emplace_back(object2);

    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(800, 600, "Gravitational_Potential", NULL, NULL);
    if(window == NULL)
    {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);
    glfwSwapInterval(1);

    if (glewInit() != GLEW_OK) {
    std::cout << "Failed to initialize GLEW" << std::endl;
    return -1;
    };

    unsigned int VBO, VAO;
    glGenBuffers(1, &VBO);
    glGenVertexArrays(1, &VAO);
    glBindVertexArray(VAO);

    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, UnitCircle.vertices.size() * sizeof(float), UnitCircle.vertices.data(), GL_STATIC_DRAW);

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * sizeof(float), (void*)0);
    glEnableVertexAttribArray(0);

    const char* vertexShaderSource = "#version 330 core\n"
    "layout (location = 0) in vec3 aPos;\n"
    "uniform vec2 aspect;\n"
    "uniform vec2 offset;\n"
    "uniform float radius;\n"
    "void main() {\n"
    "    vec2 scaled = aPos.xy * radius * aspect;\n"
    "    vec2 finalPos = scaled + offset;\n"
    "    gl_Position = vec4(finalPos, aPos.z, 1.0);\n"
    "}";


    unsigned int vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    const char* fragmentShaderSource = "#version 330 core\n"
    "out vec4 FragColor;\n"
    "void main() {\n"
    "   FragColor = vec4(.1, 0.8, 0.2, 1.0);\n"
    "}";

    unsigned int fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    unsigned int shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    float dt=0,lastFrame=0;


    while(!glfwWindowShouldClose(window))
    {
        glClear(GL_COLOR_BUFFER_BIT);

        glUseProgram(shaderProgram);

        float currentFrame = glfwGetTime();
        dt = currentFrame - lastFrame;
        lastFrame = currentFrame;
        

        int width, height;
        glfwGetFramebufferSize(window, &width, &height);
        float aspectRatio = float(width)/float(height);
        int aspectLocation = glGetUniformLocation(shaderProgram, "aspect");
        glUniform2f(aspectLocation, 1.0f / (float(width) / float(height)), 1.0f);

        glBindVertexArray(VAO);

        for (auto& object : objects) {
            object.update_parameters(dt);
            object.render(shaderProgram);
            glDrawArrays(GL_TRIANGLE_FAN, 0, object.vertices.size() / 3);
        }

        glfwPollEvents();
        glfwSwapBuffers(window);
    }

    glfwTerminate();
    return 0;
}

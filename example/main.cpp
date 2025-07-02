#include <iostream>

#include "config.yaml.hpp"

int main() {
  std::cout << "config.project.name = '" << config.project.name << "'"
            << std::endl;
}

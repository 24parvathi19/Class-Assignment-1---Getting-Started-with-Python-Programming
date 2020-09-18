{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled8.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyMO4GhNzyFQIy7cSZf2jle6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/24parvathi19/Class-Assignment-1---Getting-Started-with-Python-Programming/blob/master/list.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "cKy6ds51m5xw",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "3a09cbc7-a0a9-4b36-f080-a1f8b715dcae"
      },
      "source": [
        "def search(list,value):\n",
        "    for i in range(len(list)):\n",
        "        if list[i]==value:\n",
        "            return True\n",
        "    return False\n",
        "list = [12,\"rose\",24,\"jasmine\",6]\n",
        "value = 24\n",
        "if search(list,value):\n",
        "    print(\"element found\")\n",
        "else:\n",
        "    print(\"element not found\")    \n"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "element found\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}
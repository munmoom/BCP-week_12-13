{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPtRGkiaxc2EN6G+OYvGTW5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP-week_12-13/blob/main/1-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 27,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iwwPS-BMkRHV",
        "outputId": "68439d99-fb62-41d0-aa2c-986ad3eac551"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "26 1000 5\n",
            "Trip #1: 1.29 928.20\n",
            "27.25 873234 3000\n",
            "Trip #2: 1179.86 1415.84\n",
            "26 0 1000\n"
          ]
        }
      ],
      "source": [
        "i=0\n",
        "while True:\n",
        " inch, rot, sec = map(float, input().split())\n",
        " if rot==0:\n",
        "    break\n",
        " i+=1\n",
        " d=inch*3.1415927*(1/(12*5280))*rot\n",
        " dis=round(d,3)\n",
        " dis=format(dis,\".2f\")\n",
        "\n",
        " vel=d/(sec/3600)\n",
        " v=round(vel,3)\n",
        " v=format(v,\".2f\")\n",
        "\n",
        " print(f'Trip #{i}:',end=' ')\n",
        " print(dis, end=' ')\n",
        " print(v)\n"
      ]
    }
  ]
}
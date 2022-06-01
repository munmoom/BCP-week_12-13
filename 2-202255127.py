{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "2-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyN+s5aqiO12dB/k4ZKr7djs",
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
        "<a href=\"https://colab.research.google.com/github/munmoom/BCP-week_12-13/blob/main/2-202255127.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vQQxVCgTtJge",
        "outputId": "786314e3-d2dd-40e1-8c85-5b894e112f97"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10110111\n",
            "110000100111\n",
            "['1', '1', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1']\n"
          ]
        }
      ],
      "source": [
        "two=str(input())\n",
        "n=len(two)\n",
        "result=0\n",
        "\n",
        "\n",
        "for i in range(0,n):\n",
        "  res=int(two[i])*2**(n-1-i)\n",
        "  result+=res\n",
        "\n",
        "result=result*17\n",
        "li=[]\n",
        "\n",
        "while True:\n",
        " if result==1:\n",
        "   li.append('1')\n",
        "   break\n",
        " if result%2==0:\n",
        "   li.append('0')\n",
        " else:\n",
        "   li.append('1')\n",
        " result=result//2\n",
        "\n",
        "li.reverse()\n",
        "R=''.join(li)\n",
        "print(R)"
      ]
    }
  ]
}
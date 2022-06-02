{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "1-202255127.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPIG0Ecmh/5bV/RvNt/QOBe",
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
      "execution_count": null,
      "metadata": {
        "id": "rcs0T_-JGRO0"
      },
      "outputs": [],
      "source": [
        "n=int(input())\n",
        "for i in range(0,n):\n",
        "  A, B=map(int, input().split())\n",
        "  res=A+B\n",
        "  print(f'Case {i+1}: {res}')"
      ]
    }
  ]
}
class fibonacci():\n",
    "    def __init__(self):\n",
    "        self.quant_termos= int(input('Quantos termos da sequencia?:'))\n",
    "        self.n1=0\n",
    "        self.n2=1\n",
    "    def gerar_sequencia(self):\n",
    "        if self.quant_termos <=0:\n",
    "            return 0\n",
    "        elif self.quant_termos == 1:\n",
    "            print('Primeiro termo da sequencia é ', self.quant_termos, ':' )\n",
    "        else:\n",
    "            count=0\n",
    "            f_sqcia=[]\n",
    "            print(f\"Sequência de Fibonacci com {self.quant_termos}:\")\n",
    "            while count < self.quant_termos:\n",
    "                f_sqcia.append(self.n1)\n",
    "                nth = self.n1 + self.n2\n",
    "                self.n1 = self.n2\n",
    "                self.n2 = nth\n",
    "                count += 1\n",
    "            print(f_sqcia)\n
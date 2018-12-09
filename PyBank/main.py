{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "import os"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_in = \"Resources/budget_data.csv\"\n",
    "file_out = \"Resources/budget_summary.txt\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Total Months: 86\n",
      "Total Revenue: 38382578\n",
      "Average Revenue Change: $-2288.1976744186045\n",
      "Greatest increase in Revenue: (1926159, 'Feb-2012')\n",
      "Greatest decrease in Revenue: (-2196167, 'Sep-2013')\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(file_in) as csv_data:\n",
    "    csv_reader = csv.reader(csv_data)\n",
    "    \n",
    "    csv_dict = {}\n",
    "    pl_dict = {}\n",
    "    month_list = []\n",
    "    pl_list = []\n",
    "    \n",
    "    for row in csv_reader:\n",
    "        if row[0] != 'Date':\n",
    "            csv_dict[row[0]] = int(row[1])\n",
    "    \n",
    "    total_months = len(csv_dict)\n",
    "    total_pl = sum(csv_dict.values())\n",
    "    pl = tuple(csv_dict.values())\n",
    "    date = tuple(csv_dict.keys())\n",
    "    \n",
    "    for i in range(1, (len(pl))):\n",
    "        month_list.append(int(pl[i]) - int(pl[i - 1]))\n",
    "    \n",
    "    pl_average = sum(month_list) / total_months\n",
    "    \n",
    "    for i in range(1, (len(date))):\n",
    "        pl_dict[date[i]] = int(month_list[i - 1])\n",
    "        \n",
    "    pl_increase = max(zip(pl_dict.values(), pl_dict.keys()))\n",
    "    pl_decrease = min(zip(pl_dict.values(), pl_dict.keys()))   \n",
    "    \n",
    "    data_summary = (\n",
    "        f\"Total Months: {total_months}\\n\"\n",
    "        f\"Total Revenue: {total_pl}\\n\"\n",
    "        f\"Average Revenue Change: ${pl_average}\\n\"\n",
    "        f\"Greatest increase in Revenue: {pl_increase}\\n\"\n",
    "        f\"Greatest decrease in Revenue: {pl_decrease}\\n\"\n",
    "    )\n",
    "\n",
    "print(data_summary)\n",
    "\n",
    "with open(file_out, \"w\") as txt_file:\n",
    "    txt_file.write(data_summary)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

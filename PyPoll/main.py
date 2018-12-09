{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "from collections import Counter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_in = \"Resources/election_data.csv\"\n",
    "file_out = \"Resources/election_summary.txt\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('Khan', 'Correy', 'Li', \"O'Tooley\")\n",
      "(2218231, 704200, 492940, 105630)\n",
      "(2218231, 'Khan')\n",
      "None\n",
      "Election Results\n",
      "--------------------------\n",
      "Total Votes: 3521001\n",
      "--------------------------\n",
      "Winner: (2218231, 'Khan')\n",
      "Candidates Vote Totals\n",
      "--------------------------\n",
      "('Khan', 'Correy', 'Li', \"O'Tooley\")\n",
      "(2218231, 704200, 492940, 105630)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "with open(file_in) as csv_data:\n",
    "    csv_reader = csv.reader(csv_data)\n",
    "    \n",
    "    header_remove = next(csv_reader)\n",
    "        \n",
    "    cand_list = []\n",
    "    total_votes = 0\n",
    "    percent_vote = []\n",
    "    poll_values = []\n",
    "    votes_total = Counter()\n",
    "    \n",
    "    for row in csv_reader:\n",
    "        cand_list.append(row[2])\n",
    "    \n",
    "    total_votes = len(cand_list)\n",
    "    \n",
    "    for name in cand_list:\n",
    "        votes_total[name] += 1\n",
    "        \n",
    "    names = tuple(votes_total.keys())\n",
    "    print(names)\n",
    "    votes = tuple(votes_total.values())\n",
    "    print(votes)\n",
    "    election_winner = max(zip(votes_total.values(), votes_total.keys()))\n",
    "    print(election_winner)\n",
    "    \n",
    "    for i in votes:\n",
    "        p_vote = percent_vote.append((int(i)/total_votes))\n",
    "    print(p_vote)\n",
    "    \n",
    "    data_summary = (\n",
    "                        f\"Election Results\\n\"\n",
    "                        f\"--------------------------\\n\"\n",
    "                        f\"Total Votes: {total_votes}\\n\"\n",
    "                        f\"--------------------------\\n\"\n",
    "                        f\"Winner: {election_winner}\\n\"\n",
    "                        f\"Candidates Vote Totals\\n\"\n",
    "                        f\"--------------------------\\n\"\n",
    "                        f\"{names}\\n\"\n",
    "                        f\"{votes}\\n\"\n",
    "    )\n",
    "\n",
    "    print(data_summary)\n",
    "\n",
    "with open(file_out, \"w\") as txt_file:\n",
    "    txt_file.write(data_summary)"
   ]
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
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

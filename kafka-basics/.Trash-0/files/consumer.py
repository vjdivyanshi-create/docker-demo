{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "19cfc5e9-dbb0-434c-9a64-3ad8a7c42d1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from kafka import KafkaConsumer\n",
    "import json\n",
    "\n",
    "Consumer = KafkaConsumer(\n",
    "    \"demo-topic\",\n",
    "    bootstrap_servers = \"kafka:9092\",\n",
    "    auto_offset_reset=\"earliest\",\n",
    "    value_deserializer = lambda x: json.loads(x.decode(\"utf-8\"))\n",
    ")\n",
    "\n",
    "for msg in Consumer:\n",
    "    print(msg.value)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aa29e7e-d5d7-4c11-9fd8-05e930e2e247",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

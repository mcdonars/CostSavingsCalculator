FROM python:3
ADD CostSavingsCalculator.py /
RUN pip install pystrich
CMD [ "python", "./CostSavingsCalculator.py" ]

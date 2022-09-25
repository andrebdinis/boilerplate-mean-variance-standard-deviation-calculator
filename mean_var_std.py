import numpy as np
import pprint

def calculate(inputList):
  
  if( len(inputList) < 9): raise ValueError('List must contain nine numbers.')

  flat = np.array(inputList)
  matrix = flat.reshape(3,3)

  mean = [
    list( matrix.mean(axis=0) ),
    list( matrix.mean(axis=1) ),
    flat.mean()
  ]

  variance = [
    list( matrix.var(axis=0) ),
    list( matrix.var(axis=1) ),
    flat.var()
  ]

  standard_deviation = [
    list( matrix.std(axis=0) ),
    list( matrix.std(axis=1) ),
    flat.std()
  ]

  max = [
    list( matrix.max(axis=0) ),
    list( matrix.max(axis=1) ),
    flat.max()
  ]

  min = [
    list( matrix.min(axis=0) ),
    list( matrix.min(axis=1) ),
    flat.min()
  ]

  sum = [
    list( matrix.sum(axis=0) ),
    list( matrix.sum(axis=1) ),
    flat.sum()
  ]

  calculations = {
    'mean': mean,
    'variance': variance,
    'standard deviation': standard_deviation,
    'max': max,
    'min': min,
    'sum': sum
  }

  # Print
  printCalculations(inputList, flat, matrix, calculations)
  
  return calculations


def printCalculations(inputList, flat, matrix, calculations):
  print()
  #chars = '/'.ljust(50,'/')
  #print(chars)
  print('List:', inputList)
  print('NumPy Flattened Array:', flat)
  print('NumPy Matrix 3x3:\n', matrix)
  print('Calculations:')
  pprint.pprint((calculations))
  print()
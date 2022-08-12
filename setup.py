from distutils.core import setup

setup(
  name = 'price_predictor',
  packages = ['price_predictor'],
  version = '1.0.0',
  license='MIT',
  description = 'Quickly predict the future prices of financial instruments with a customizable LSTM Recurrent Neural Network',
  author = 'Ludovico Lemmma', 
  author_email = 'lwdovico@protonmail.com',
  url = 'https://github.com/ludovicolemma/price-predictor',
  download_url = 'https://github.com/ludovicolemma/price-predictor/archive/refs/tags/v1.0.1.tar.gz',
  keywords = ['LSTM',
              'Machine Learning',
              'Market Price Prediction', 
              'Stock Price Prediction', 
              'Financial Forecasting'],
  install_requires=[
          'numpy',
          'pandas',
          'matplotlib',
          'sklearn',
          'tensorflow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Developers',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Software Development :: Build Tools',
    'Topic :: Office/Business :: Financial :: Investment',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
  ],
)

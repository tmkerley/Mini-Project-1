# Known Bugs

If the interval set to anything other than "1wk" the program breaks.
    approx line 23 : data = yf.download("NFLX", interval="1d")

    Exception in thread Thread-7 (_run_via_pool):
    Traceback (most recent call last):
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\threading.py", line 1016, in _bootstrap_inner    self.run()
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\threading.py", line 953, in run
        self._target(*self._args, **self._kwargs)
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\site-packages\multitasking\__init__.py", line 104, in _run_via_pool
        return callee(*args, **kwargs)
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\site-packages\yfinance\multi.py", line 169, in _download_one_threaded
        data = _download_one(ticker, start, end, auto_adjust, back_adjust,
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\site-packages\yfinance\multi.py", line 181, in _download_one
        return Ticker(ticker).history(period=period, interval=interval,
    File "C:\Users\Thomas\AppData\Local\Programs\Python\Python310\lib\site-packages\yfinance\base.py", line 247, in history
        df.index = df.index.tz_localize("UTC").tz_convert(
    AttributeError: 'Index' object has no attribute 'tz_localize'

Initially tried to do a date range as per the video Mini Project 1 Started, time stamp: 36:03
https://youtu.be/Q39j7d_7JVo?t=2163

If you look at the commits you might be able to see how I even implemented a function to automatically get the past 10 business days using the datetime package.

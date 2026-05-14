# SignalDraw ISB

A Jupyter widget for drawing and analyzing signals using `anywidget`.

## Installation

```bash
pip install git+https://github.com/MSMRo/signalDraw-isb.git
#pip install signaldraw-isb  # Proximamente
```

## Usage

```python
from signaldraw_isb import SignalDraw

ui = SignalDraw()
ui
```

Then you can access the signals generated:
```python
# Returns a numpy array with the result signal
ui.signal_numpy 

# Returns a list of numpy arrays for all individual signals
ui.signals_numpy 
```

![](./imgs/ui.png)

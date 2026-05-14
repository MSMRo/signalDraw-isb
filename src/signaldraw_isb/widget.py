#!/usr/bin/env python
# coding: utf-8

# In[1]:


import anywidget
import traitlets
import numpy as np


class SignalDraw(anywidget.AnyWidget):

    # =====================================================
    # TRAITLETS
    # =====================================================

    # legacy
    signal = traitlets.List([]).tag(sync=True)

    # new api
    signals = traitlets.List([]).tag(sync=True)

    fs = traitlets.List([]).tag(sync=True)

    # =====================================================
    # FRONTEND
    # =====================================================

    _esm = r"""

export function render({ model, el }) {

    // =====================================================
    // COLORS
    // =====================================================

    const COLORS = [
        "#0066ff",
        "#ff0000",
        "#00aa00",
        "#ff9900",
        "#9900ff"
    ];

    // =====================================================
    // ROOT
    // =====================================================

    const root = document.createElement("div");

    root.style.width = "100%";
    root.style.maxWidth = "1800px";
    root.style.background = "#efefef";
    root.style.padding = "8px";
    root.style.fontFamily = "Arial";
    root.style.boxSizing = "border-box";

    el.appendChild(root);

    // =====================================================
    // TOPBAR
    // =====================================================

    const topbar = document.createElement("div");

    topbar.style.display = "flex";
    topbar.style.alignItems = "center";
    topbar.style.gap = "12px";
    topbar.style.background = "white";
    topbar.style.padding = "8px";
    topbar.style.borderRadius = "6px";
    topbar.style.marginBottom = "8px";

    root.appendChild(topbar);

    // =====================================================
    // TITLE
    // =====================================================

    const title = document.createElement("h2");

    title.innerText = "SignalDraw-ISB";

    title.style.margin = "0";
    title.style.color = "#0066ff";
    title.style.marginRight = "auto";

    topbar.appendChild(title);

    // =====================================================
    // #SIGNALS
    // =====================================================

    const label =
        document.createElement("label");

    label.innerText = "#Signals";

    topbar.appendChild(label);

    const select =
        document.createElement("select");

    for(let i=1;i<=5;i++) {

        const op =
            document.createElement("option");

        op.value = i;
        op.text = i;

        if(i===1)
            op.selected = true;

        select.appendChild(op);
    }

    topbar.appendChild(select);

    // =====================================================
    // GENERATE
    // =====================================================

    const btn =
        document.createElement("button");

    btn.innerText = "GENERATE";

    btn.style.padding = "6px 12px";
    btn.style.background = "#0066ff";
    btn.style.color = "white";
    btn.style.border = "none";
    btn.style.borderRadius = "5px";
    btn.style.cursor = "pointer";

    topbar.appendChild(btn);

    // =====================================================
    // RESET
    // =====================================================

    const resetBtn =
        document.createElement("button");

    resetBtn.innerText = "RESET";

    resetBtn.style.padding = "6px 12px";
    resetBtn.style.background = "#ff4444";
    resetBtn.style.color = "white";
    resetBtn.style.border = "none";
    resetBtn.style.borderRadius = "5px";
    resetBtn.style.cursor = "pointer";

    topbar.appendChild(resetBtn);

    // =====================================================
    // MAIN
    // =====================================================

    const main = document.createElement("div");

    main.style.display = "flex";
    main.style.gap = "8px";

    root.appendChild(main);

    // =====================================================
    // LEFT
    // =====================================================

    const left =
        document.createElement("div");

    left.style.width = "25%";
    left.style.display = "flex";
    left.style.flexDirection = "column";
    left.style.gap = "8px";
    left.style.maxHeight = "1400px";
    left.style.overflowY = "auto";

    main.appendChild(left);

    // =====================================================
    // CENTER
    // =====================================================

    const center =
        document.createElement("div");

    center.style.width = "35%";
    center.style.display = "flex";
    center.style.flexDirection = "column";
    center.style.gap = "8px";

    main.appendChild(center);

    // =====================================================
    // RIGHT
    // =====================================================

    const right =
        document.createElement("div");

    right.style.width = "40%";
    right.style.display = "flex";
    right.style.flexDirection = "column";
    right.style.gap = "8px";

    main.appendChild(right);

    // =====================================================
    // CREATE CARD
    // =====================================================

    function createCard(titleText,height=260) {

        const card =
            document.createElement("div");

        card.style.background = "white";
        card.style.padding = "6px";
        card.style.borderRadius = "6px";

        const title =
            document.createElement("div");

        title.innerText = titleText;

        title.style.fontWeight = "bold";
        title.style.marginBottom = "4px";

        card.appendChild(title);

        const svg =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "svg"
            );

        svg.setAttribute("width","620");
        svg.setAttribute("height",height);

        svg.style.border =
            "1px solid #dddddd";

        card.appendChild(svg);

        return {
            card,
            svg
        };
    }

    // =====================================================
    // RESULT PLOTS
    // =====================================================

    const resultPlot =
        createCard(
            "Señal resultante",
            260
        );

    right.appendChild(
        resultPlot.card
    );

    const fftPlot =
        createCard(
            "FFT",
            260
        );

    right.appendChild(
        fftPlot.card
    );

    const stftPlot =
        createCard(
            "STFT Spectrogram",
            320
        );

    right.appendChild(
        stftPlot.card
    );

    // =====================================================
    // INPUT
    // =====================================================

    function createInput(label,value) {

        const c =
            document.createElement("div");

        c.style.display = "flex";
        c.style.flexDirection = "column";
        c.style.marginBottom = "6px";

        const l =
            document.createElement("label");

        l.innerText = label;

        l.style.fontSize = "12px";

        const i =
            document.createElement("input");

        i.type = "number";
        i.value = value;

        i.style.padding = "4px";

        c.appendChild(l);
        c.appendChild(i);

        return {
            container:c,
            input:i
        };
    }

    // =====================================================
    // SLIDER
    // =====================================================

    function createSlider(
        label,
        value,
        minVal=-5,
        maxVal=5
    ) {

        const c =
            document.createElement("div");

        c.style.display = "flex";
        c.style.flexDirection = "column";
        c.style.marginBottom = "6px";

        const row =
            document.createElement("div");

        row.style.display = "flex";

        row.style.justifyContent =
            "space-between";

        const l =
            document.createElement("label");

        l.innerText = label;

        const valueText =
            document.createElement("span");

        valueText.innerText =
            parseFloat(value).toFixed(1);

        valueText.style.fontWeight = "bold";
        valueText.style.color = "#0066ff";

        row.appendChild(l);
        row.appendChild(valueText);

        const s =
            document.createElement("input");

        s.type = "range";

        s.min = minVal;
        s.max = maxVal;
        s.step = 0.1;
        s.value = value;

        s.addEventListener("input",()=>{

            valueText.innerText =
                parseFloat(s.value).toFixed(1);
        });

        c.appendChild(row);
        c.appendChild(s);

        return {
            container:c,
            slider:s
        };
    }

    // =====================================================
    // GRID
    // =====================================================

    function drawGrid(
        svg,
        w,
        h
    ) {

        svg.innerHTML = "";

        for(let x=50;x<w;x+=40) {

            const line =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "line"
                );

            line.setAttribute("x1",x);
            line.setAttribute("y1",10);

            line.setAttribute("x2",x);
            line.setAttribute("y2",h-30);

            line.setAttribute(
                "stroke",
                "#ededed"
            );

            svg.appendChild(line);
        }

        for(let y=20;y<h-30;y+=40) {

            const line =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "line"
                );

            line.setAttribute("x1",50);
            line.setAttribute("y1",y);

            line.setAttribute("x2",w);
            line.setAttribute("y2",y);

            line.setAttribute(
                "stroke",
                "#ededed"
            );

            svg.appendChild(line);
        }

        const xAxis =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "line"
            );

        xAxis.setAttribute("x1",50);
        xAxis.setAttribute("y1",h/2);

        xAxis.setAttribute("x2",w);
        xAxis.setAttribute("y2",h/2);

        xAxis.setAttribute(
            "stroke",
            "#666"
        );

        svg.appendChild(xAxis);

        const yAxis =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "line"
            );

        yAxis.setAttribute("x1",50);
        yAxis.setAttribute("y1",10);

        yAxis.setAttribute("x2",50);
        yAxis.setAttribute("y2",h-30);

        yAxis.setAttribute(
            "stroke",
            "#666"
        );

        svg.appendChild(yAxis);
    }

    // =====================================================
    // DRAW SIGNAL
    // =====================================================

    function drawSignal(
        svg,
        signal,
        color,
        totalTime
    ) {

        const w =
            parseInt(
                svg.getAttribute("width")
            );

        const h =
            parseInt(
                svg.getAttribute("height")
            );

        drawGrid(svg,w,h);

        let peak =
            Math.max(
                ...signal.map(
                    v=>Math.abs(v)
                )
            );

        if(peak < 0.001)
            peak = 1;

        const scale =
            (h*0.35)/peak;

        let path = "";

        for(let i=0;i<signal.length;i++) {

            const x =
                50 +
                i*((w-70)/signal.length);

            const y =
                h/2 -
                signal[i]*scale;

            if(i===0) {

                path += `M ${x} ${y}`;

            } else {

                path += ` L ${x} ${y}`;
            }
        }

        const curve =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "path"
            );

        curve.setAttribute("d",path);

        curve.setAttribute(
            "stroke",
            color
        );

        curve.setAttribute(
            "stroke-width",
            "2"
        );

        curve.setAttribute(
            "fill",
            "none"
        );

        svg.appendChild(curve);

        // PEAK

        const txt =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "text"
            );

        txt.setAttribute("x",w-140);
        txt.setAttribute("y","18");

        txt.setAttribute(
            "font-size",
            "11"
        );

        txt.textContent =
            "Peak: ±" +
            peak.toFixed(2);

        svg.appendChild(txt);

        // TIME LABELS

        for(let i=0;i<=10;i++) {

            const t =
                i * totalTime / 10;

            const x =
                50 +
                i*((w-70)/10);

            const txt =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "text"
                );

            txt.setAttribute("x",x-8);
            txt.setAttribute("y",h-12);

            txt.setAttribute(
                "font-size",
                "10"
            );

            txt.textContent =
                t.toFixed(1);

            svg.appendChild(txt);
        }
    }

    // =====================================================
    // FFT
    // =====================================================

    function computeFFT(signal, fs) {

        const N = signal.length;

        const halfN =
            Math.floor(N/2);

        let freqs = [];
        let mags = [];

        for(let k=0;k<halfN;k++) {

            let re = 0;
            let im = 0;

            for(let n=0;n<N;n++) {

                const angle =
                    2*Math.PI*k*n/N;

                re +=
                    signal[n] *
                    Math.cos(angle);

                im -=
                    signal[n] *
                    Math.sin(angle);
            }

            const mag =
                Math.sqrt(re*re+im*im)/N;

            freqs.push(k*fs/N);

            mags.push(mag);
        }

        return {
            freqs,
            mags
        };
    }

    // =====================================================
    // DRAW FFT
    // =====================================================

    function drawFFT(
    svg,
    freqs,
    mags,
    fs
) {

    const w =
        parseInt(
            svg.getAttribute("width")
        );

    const h =
        parseInt(
            svg.getAttribute("height")
        );

    drawGrid(svg,w,h);

    let maxVal =
        Math.max(...mags);

    if(maxVal < 1e-9)
        maxVal = 1;

    const norm =
        mags.map(v=>v/maxVal);

    // ==========================================
    // AUTO X SCALE
    // ==========================================

    const significant =
        freqs.filter(
            (f,i)=>norm[i] > 0.1
        );

    let maxFreq;

    if(significant.length>0) {

        maxFreq =
            Math.max(...significant)*1.4;

    } else {

        maxFreq = fs/2;
    }

    if(maxFreq < 20)
        maxFreq = 20;

    // ==========================================
    // SPECTRUM
    // ==========================================

    for(let i=0;i<freqs.length;i++) {

        if(freqs[i] > maxFreq)
            continue;

        const x =
            50 +
            (freqs[i]/maxFreq) *
            (w-70);

        const y =
            h-30 -
            norm[i]*(h*0.7);

        const line =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "line"
            );

        line.setAttribute("x1",x);
        line.setAttribute("y1",h-30);

        line.setAttribute("x2",x);
        line.setAttribute("y2",y);

        line.setAttribute(
            "stroke",
            "#00aa00"
        );

        line.setAttribute(
            "stroke-width",
            "2"
        );

        svg.appendChild(line);

        // ======================================
        // PEAK LABELS
        // ======================================

        if(norm[i] > 0.3) {

            const txt =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "text"
                );

            txt.setAttribute("x",x-10);
            txt.setAttribute("y",y-5);

            txt.setAttribute(
                "font-size",
                "10"
            );

            txt.textContent =
                freqs[i].toFixed(1)+"Hz";

            svg.appendChild(txt);
        }
    }

    // ==========================================
    // X LABELS
    // ==========================================

    for(let i=0;i<=10;i++) {

        const f =
            i * maxFreq / 10;

        const x =
            50 +
            i*((w-70)/10);

        const txt =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "text"
            );

        txt.setAttribute("x",x-8);
        txt.setAttribute("y",h-10);

        txt.setAttribute(
            "font-size",
            "10"
        );

        txt.textContent =
            f.toFixed(1);

        svg.appendChild(txt);
    }

    // ==========================================
    // Y LABELS
    // ==========================================

    for(let i=0;i<=5;i++) {

        const val =
            1 - i/5;

        const y =
            20 +
            i*((h-50)/5);

        const txt =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "text"
            );

        txt.setAttribute("x","8");
        txt.setAttribute("y",y+4);

        txt.setAttribute(
            "font-size",
            "10"
        );

        txt.textContent =
            val.toFixed(1);

        svg.appendChild(txt);
    }

    // ==========================================
    // TITLES
    // ==========================================

    const xTitle =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

    xTitle.setAttribute("x",w/2-40);
    xTitle.setAttribute("y",h-2);

    xTitle.setAttribute(
        "font-size",
        "12"
    );

    xTitle.textContent =
        "Frequency (Hz)";

    svg.appendChild(xTitle);

    const yTitle =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

    yTitle.setAttribute(
        "transform",
        "rotate(-90)"
    );

    yTitle.setAttribute(
        "x",
        -h/2
    );

    yTitle.setAttribute(
        "y",
        "14"
    );

    yTitle.setAttribute(
        "font-size",
        "12"
    );

    yTitle.textContent =
        "Normalized Magnitude";

    svg.appendChild(yTitle);
}

    // =====================================================
    // STFT
    // =====================================================

    function computeSTFT(
        signal,
        fs,
        windowSize=256,
        hopSize=64
    ) {

        let spectrogram = [];

        for(
            let start=0;
            start<signal.length-windowSize;
            start+=hopSize
        ) {

            const segment =
                signal.slice(
                    start,
                    start+windowSize
                );

            let mags = [];

            for(let k=0;k<windowSize/2;k++) {

                let re = 0;
                let im = 0;

                for(let n=0;n<windowSize;n++) {

                    const angle =
                        2*Math.PI*k*n/windowSize;

                    re +=
                        segment[n] *
                        Math.cos(angle);

                    im -=
                        segment[n] *
                        Math.sin(angle);
                }

                const mag =
                    Math.sqrt(re*re+im*im);

                mags.push(mag);
            }

            spectrogram.push(mags);
        }

        return spectrogram;
    }

    // =====================================================
    // DRAW STFT
    // =====================================================
    function drawSTFT(
    svg,
    spectrogram,
    fs,
    totalTime
) {

    svg.innerHTML = "";

    const w =
        parseInt(
            svg.getAttribute("width")
        );

    const h =
        parseInt(
            svg.getAttribute("height")
        );

    const cols =
        spectrogram.length;

    const rows =
        spectrogram[0].length;

    // ==========================================
    // MAX VALUE
    // ==========================================

    let maxVal = 0;

    for(let x=0;x<cols;x++) {

        for(let y=0;y<rows;y++) {

            if(
                spectrogram[x][y]
                > maxVal
            ) {

                maxVal =
                    spectrogram[x][y];
            }
        }
    }

    // ==========================================
    // AUTO FREQ SCALE
    // ==========================================

    let maxRow = rows;

    for(let y=rows-1;y>=0;y--) {

        let found = false;

        for(let x=0;x<cols;x++) {

            const val =
                spectrogram[x][y]/maxVal;

            if(val > 0.05) {

                found = true;
                break;
            }
        }

        if(found) {

            maxRow = y + 8;
            break;
        }
    }

    if(maxRow < 16)
        maxRow = 16;

    maxRow =
        Math.min(maxRow,rows);

    // ==========================================
    // GRID
    // ==========================================

    for(let x=50;x<w;x+=40) {

        const line =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "line"
            );

        line.setAttribute("x1",x);
        line.setAttribute("y1",10);

        line.setAttribute("x2",x);
        line.setAttribute("y2",h-30);

        line.setAttribute(
            "stroke",
            "#dddddd"
        );

        svg.appendChild(line);
    }

    for(let y=20;y<h-30;y+=40) {

        const line =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "line"
            );

        line.setAttribute("x1",50);
        line.setAttribute("y1",y);

        line.setAttribute("x2",w);
        line.setAttribute("y2",y);

        line.setAttribute(
            "stroke",
            "#dddddd"
        );

        svg.appendChild(line);
    }

    // ==========================================
    // HEATMAP
    // ==========================================

    for(let x=0;x<cols;x++) {

        for(let y=0;y<maxRow;y++) {

            const val =
                spectrogram[x][y]/maxVal;

            const logVal =
                Math.log10(
                    1 + 9*val
                );

            const rect =
                document.createElementNS(
                    "http://www.w3.org/2000/svg",
                    "rect"
                );

            const px =
                50 +
                x*((w-70)/cols);

            const py =
                h-30 -
                ((y/maxRow)*(h-40));

            rect.setAttribute("x",px);
            rect.setAttribute("y",py);

            rect.setAttribute(
                "width",
                (w-70)/cols + 1
            );

            rect.setAttribute(
                "height",
                (h-40)/maxRow + 1
            );

            const r =
                Math.floor(
                    255*logVal
                );

            const g =
                Math.floor(
                    180*logVal
                );

            const b =
                Math.floor(
                    255*(1-logVal)
                );

            rect.setAttribute(
                "fill",
                `rgb(${r},${g},${b})`
            );

            svg.appendChild(rect);
        }
    }

    // ==========================================
    // AXES
    // ==========================================

    const xAxis =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "line"
        );

    xAxis.setAttribute("x1",50);
    xAxis.setAttribute("y1",h-30);

    xAxis.setAttribute("x2",w);
    xAxis.setAttribute("y2",h-30);

    xAxis.setAttribute(
        "stroke",
        "#666"
    );

    svg.appendChild(xAxis);

    const yAxis =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "line"
        );

    yAxis.setAttribute("x1",50);
    yAxis.setAttribute("y1",10);

    yAxis.setAttribute("x2",50);
    yAxis.setAttribute("y2",h-30);

    yAxis.setAttribute(
        "stroke",
        "#666"
    );

    svg.appendChild(yAxis);

    // ==========================================
    // X LABELS
    // ==========================================

    for(let i=0;i<=10;i++) {

        const t =
            i * totalTime / 10;

        const x =
            50 +
            i*((w-70)/10);

        const txt =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "text"
            );

        txt.setAttribute("x",x-8);
        txt.setAttribute("y",h-10);

        txt.setAttribute(
            "font-size",
            "10"
        );

        txt.textContent =
            t.toFixed(1);

        svg.appendChild(txt);
    }

    // ==========================================
    // Y LABELS
    // ==========================================

    const maxFreq =
        (maxRow/rows) *
        (fs/2);

    for(let i=0;i<=5;i++) {

        const f =
            i * maxFreq / 5;

        const y =
            h-30 -
            i*((h-40)/5);

        const txt =
            document.createElementNS(
                "http://www.w3.org/2000/svg",
                "text"
            );

        txt.setAttribute("x","5");
        txt.setAttribute("y",y+4);

        txt.setAttribute(
            "font-size",
            "10"
        );

        txt.textContent =
            f.toFixed(0);

        svg.appendChild(txt);
    }

    // ==========================================
    // TITLES
    // ==========================================

    const xTitle =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

    xTitle.setAttribute("x",w/2-30);
    xTitle.setAttribute("y",h-2);

    xTitle.setAttribute(
        "font-size",
        "12"
    );

    xTitle.textContent =
        "Time (s)";

    svg.appendChild(xTitle);

    const yTitle =
        document.createElementNS(
            "http://www.w3.org/2000/svg",
            "text"
        );

    yTitle.setAttribute(
        "transform",
        "rotate(-90)"
    );

    yTitle.setAttribute(
        "x",
        -h/2
    );

    yTitle.setAttribute(
        "y",
        "14"
    );

    yTitle.setAttribute(
        "font-size",
        "12"
    );

    yTitle.textContent =
        "Frequency (Hz)";

    svg.appendChild(yTitle);
}
    

    // =====================================================
    // CONFIGS
    // =====================================================

    let configs = [];

    // =====================================================
    // SAVE STATE
    // =====================================================

    function saveCurrentState() {

        return configs.map(cfg => ({

            fs:
                cfg.fs.input.value,

            freq:
                cfg.freq.input.value,

            amp:
                cfg.amp.slider.value,

            phase:
                cfg.phase.input.value,

            offset:
                cfg.offset.slider.value,

            startTime:
                cfg.startTime.input.value,

            endTime:
                cfg.endTime.input.value
        }));
    }

    // =====================================================
    // BUILD UI
    // =====================================================

    function buildUI(previousState=[]) {

        left.innerHTML = "";
        center.innerHTML = "";

        configs = [];

        const n =
            parseInt(select.value);

        for(let i=0;i<n;i++) {

            const prev =
                previousState[i] || {};

            const card =
                document.createElement("div");

            card.style.background = "white";
            card.style.padding = "8px";
            card.style.borderRadius = "6px";

            card.style.borderLeft =
                "4px solid " + COLORS[i];

            const title =
                document.createElement("div");

            title.innerText =
                "Signal " + (i+1);

            title.style.fontWeight = "bold";
            title.style.color = COLORS[i];

            card.appendChild(title);

            const fs =
                createInput(
                    "Fs",
                    prev.fs || 1000
                );

            const freq =
                createInput(
                    "Frequency",
                    prev.freq || (5+i)
                );

            const amp =
                createSlider(
                    "Amplitude",
                    prev.amp || 1,
                    0,
                    5
                );

            const phase =
                createInput(
                    "Phase",
                    prev.phase || 0
                );

            const offset =
                createSlider(
                    "Offset DC",
                    prev.offset || 0,
                    -5,
                    5
                );

            const startTime =
                createInput(
                    "Start Time (s)",
                    prev.startTime || 0
                );

            const endTime =
                createInput(
                    "End Time (s)",
                    prev.endTime || 6
                );

            card.appendChild(fs.container);
            card.appendChild(freq.container);
            card.appendChild(amp.container);
            card.appendChild(phase.container);
            card.appendChild(offset.container);
            card.appendChild(startTime.container);
            card.appendChild(endTime.container);

            left.appendChild(card);

            const graph =
                createCard(
                    "Signal " + (i+1),
                    180
                );

            center.appendChild(
                graph.card
            );

            configs.push({

                fs,
                freq,
                amp,
                phase,
               offset,
                startTime,
                endTime,
                svg:graph.svg,
                color:COLORS[i]
            });
        }
    }

    // =====================================================
    // GENERATE
    // =====================================================

    function generate() {

        let totalTime = 0;

        configs.forEach(cfg => {

            const endT =
                parseFloat(
                    cfg.endTime.input.value
                );

            if(endT > totalTime)
                totalTime = endT;
        });

        const commonFs = 1000;

        const totalSamples =
            Math.floor(
                totalTime * commonFs
            );

        let total =
            new Array(totalSamples).fill(0);

        let allSignals = [];

        let allFs = [];

        configs.forEach(cfg => {

            const fs =
                parseFloat(
                    cfg.fs.input.value
                );

            const amp =
                parseFloat(
                    cfg.amp.slider.value
                );

            const freq =
                parseFloat(
                    cfg.freq.input.value
                );

            const phase =
                parseFloat(
                    cfg.phase.input.value
                );

            const offset =
                parseFloat(
                    cfg.offset.slider.value
                );

            const startT =
                parseFloat(
                    cfg.startTime.input.value
                );

            const endT =
                parseFloat(
                    cfg.endTime.input.value
                );

            let signal =
                new Array(totalSamples).fill(0);

            for(let i=0;i<totalSamples;i++) {

                const t = i/commonFs;

                if(
                    t >= startT &&
                    t <= endT
                ) {

                    signal[i] =
                        offset +
                        amp *
                        Math.sin(
                            2*Math.PI*
                            freq*
                            (t-startT)+
                            phase
                        );
                }
            }

            allSignals.push(signal);

            allFs.push(fs);

            total =
                total.map(
                    (v,i)=>v+signal[i]
                );

            drawSignal(
                cfg.svg,
                signal,
                cfg.color,
                totalTime
            );
        });

        // =====================================================
        // RESULT SIGNAL FIRST
        // =====================================================

        allSignals.unshift(total);

        // =====================================================
        // COMMON FS
        // =====================================================

        const allEqualFs =
            allFs.every(
                v => v === allFs[0]
            );

        if(allEqualFs) {

            allFs.unshift(allFs[0]);

        } else {

            allFs.unshift(0);
        }

        // =====================================================
        // DRAW RESULT
        // =====================================================

        drawSignal(
            resultPlot.svg,
            total,
            "#0066ff",
            totalTime
        );

        // =====================================================
        // FFT
        // =====================================================

        const fft =
            computeFFT(
                total,
                commonFs
            );

        drawFFT(
            fftPlot.svg,
            fft.freqs,
            fft.mags,
            commonFs
        );

        // =====================================================
        // STFT
        // =====================================================

        const spectrogram =
            computeSTFT(
                total,
                commonFs
            );

        drawSTFT(
            stftPlot.svg,
            spectrogram,
            commonFs,
            totalTime
        );

        // =====================================================
        // SYNC
        // =====================================================

        model.set(
            "signal",
            total
        );

        model.set(
            "signals",
            allSignals
        );

        model.set(
            "fs",
            allFs
        );

        model.save_changes();
    }

    // =====================================================
    // EVENTS
    // =====================================================

    select.addEventListener(
        "change",
        ()=>{

            const prev =
                saveCurrentState();

            buildUI(prev);

            generate();
        }
    );

    btn.addEventListener(
        "click",
        generate
    );

    resetBtn.addEventListener(
        "click",
        ()=>{

            buildUI();

            generate();
        }
    );

    // =====================================================
    // INIT
    // =====================================================

    buildUI();

    generate();
}
"""

    # =====================================================
    # NUMPY HELPERS
    # =====================================================

    @property
    def signal_numpy(self):

        if len(self.signals) > 0:

            return np.array(self.signals[0])

        return np.array([])


    @property
    def signals_numpy(self):

        return [
            np.array(s)
            for s in self.signals
        ]


# =====================================================
# WIDGET EXPORTS
# =====================================================

__all__ = ["SignalDraw"]



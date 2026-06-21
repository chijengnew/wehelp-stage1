function func1(name) {
    let chars = {
        "悟空": [0, 0, 0],
        "辛巴": [-3, 3, 0],
        "丁滿": [-1, 4, 1],
        "貝吉塔": [-4, -1, 0],
        "特南克斯": [1, -2, 0],
        "弗利沙": [4, -1, 1]
        };
    
    let tx = chars[name][0];
    let ty = chars[name][1];
    let ts = chars[name][2];
    
    let distances = {};
    
    for (let c in chars) {
        if (c === name) {
            continue;
            }
            
        let cx = chars[c][0];
        let cy = chars[c][1];
        let cs = chars[c][2];
        
        let dx = tx - cx;
        if (dx < 0) {
            dx = 0 - dx;
            }
            
        let dy = ty - cy;
        if (dy < 0) {
            dy = 0 - dy;
            }
            
        let dist = dx + dy;
        if (ts !== cs) {
            dist = dist + 2;
            }
            
        distances[c] = dist;
        }

    let max_d = -1;
    let min_d = 9999;
    for (let c in distances) {
        if (distances[c] > max_d) {
            max_d = distances[c];
            }
        if (distances[c] < min_d) {
            min_d = distances[c];
            }
        }

    let farthest = "";
    let closest = "";
    for (let c in distances) {
        if (distances[c] === max_d) {
            if (farthest === "") {
                farthest = c;
            } else {
                farthest = farthest + "、" + c;
            }
            }
                
        if (distances[c] === min_d) {
            if (closest === "") {
                closest = c;
            } else {
                closest = closest + "、" + c;
            }
            }
        }

    console.log("最遠" + farthest + ";最近" + closest);
}

func1("辛巴");
func1("悟空");
func1("弗利沙");
func1("特南克斯");


let bookings = {};

function func2(ss, start, end, criteria) {
    if (Object.keys(bookings).length === 0) {
        for (let i = 0; i < ss.length; i++) {
            bookings[ss[i]["name"]] = [];
        }
    }

    let op = "";
    if (criteria.includes(">=")) {
        op = ">=";
    } else if (criteria.includes("<=")) {
        op = "<=";
    } else if (criteria.includes("=")) {
        op = "=";
    }

    let parts = criteria.split(op);
    let field = parts[0];
    let value = parts[1];

    if (op !== "=") {
        value = parseFloat(value);
        }

    let best = null;

    for (let i = 0; i < ss.length; i++) {
        let s = ss[i];
        let conflict = false;
        let b_list = bookings[s["name"]];
        
        for (let j = 0; j < b_list.length; j++) {
            let b = b_list[j];
            if (start < b[1]) {
                if (end > b[0]) {
                    conflict = true;
                }
            }
        }
        
        if (conflict === false) {
            let val = s[field];
            let match = false;

            if (op === ">=") {
                if (val >= value) {
                    match = true;
                }
            } else if (op === "<=") {
                if (val <= value) {
                    match = true;
                }
            } else if (op === "=") {
                if (String(val) === String(value)) {
                    match = true;
                }
            }

            if (match === true) {
                if (best === null) {
                    best = s;
                } else {
                    if (op === ">=") {
                        if (val < best[field]) {
                            best = s;
                        }
                    } else if (op === "<=") {
                        if (val > best[field]) {
                            best = s;
                        }
                    }
                }
            }
        }
    }

    if (best !== null) {
        bookings[best["name"]].push([start, end]);
        console.log(best["name"]);
    } else {
        console.log("Sorry");
    }
}

const services = [
    {"name": "S1", "r": 4.5, "c": 1000},
    {"name": "S2", "r": 3, "c": 1200},
    {"name": "S3", "r": 3.8, "c": 800}
    ];

func2(services, 15, 17, "c>=800");
func2(services, 11, 13, "r<=4");
func2(services, 10, 12, "name=S3");
func2(services, 15, 18, "r>=4.5");
func2(services, 16, 18, "r>=4");
func2(services, 13, 17, "name=S1");
func2(services, 8, 9, "c<=1500");


function func3(index) {
    let val = 25;
    let step = 0;
    
    for (let i = 0; i < index; i++) {
        if (step === 0) {
            val = val - 2;
        } else if (step === 1) {
            val = val - 3;
        } else if (step === 2) {
            val = val + 1;
        } else if (step === 3) {
            val = val + 2;
        }
            
        step = step + 1;
        if (step === 4) {
            step = 0;
        }
    }
            
    console.log(val);
}

func3(1);
func3(5);
func3(10);
func3(30);


function func4(sp, stat, n) {
    let best = -1;
    let min_left = 9999;
    
    for (let i = 0; i < sp.length; i++) {
        if (stat[i] === "0") {
            if (sp[i] >= n) {
                let left = sp[i] - n;
                if (left < min_left) {
                    min_left = left;
                    best = i;
                }
            }
        }
    }
                    
    if (best === -1) {
        let max_s = -1;
        for (let i = 0; i < sp.length; i++) {
            if (stat[i] === "0") {
                if (sp[i] > max_s) {
                    max_s = sp[i];
                    best = i;
                }
            }
        }
    }
                    
    console.log(best);
}

func4([3, 1, 5, 4, 3, 2], "101000", 2);
func4([1, 0, 5, 1, 3], "10100", 4);
func4([4, 6, 5, 8], "1000", 4);
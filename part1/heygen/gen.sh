#!/bin/zsh
gen() {
  n=$1; text=$2
  python3 - "$text" > req_$n.json <<'PY'
import json,sys
print(json.dumps({"type":"avatar","avatar_id":"2571e80472c740fd823dbe4473ae6253","voice_id":"6f09cad7796d4aa0b1458c35a597023f","script":sys.argv[1],"aspect_ratio":"9:16","resolution":"1080p","fit":"cover","engine":{"type":"avatar_v"}}))
PY
  heygen video create --wait --timeout 40m -d req_$n.json > res_$n.json 2>&1
  url=$(python3 -c "import json;d=json.load(open('res_$n.json'))['data'];print(d.get('video_url') or '')" 2>/dev/null)
  [ -n "$url" ] && curl -sL "$url" -o scene_$n.mp4 && echo "scene $n done" || echo "scene $n FAILED"
}
gen 1 "I am Arric. In the insurance business since 1994, and today we are breaking down the best Medigap plans for 2027." &
gen 2 "We start with Medicare Supplement Plan G. It remains the most popular policy nationwide because it offers the most comprehensive coverage." &
gen 3 "With Plan G, your only out-of-pocket medical responsibility is the small annual Medicare Part B deductible. That is it." &
gen 4 "Once you pay that deductible, all other covered hospital and outpatient medical bills are covered at one hundred percent." &
gen 5 "Because coverage is so complete, premiums are higher. It is perfect if you see doctors frequently and want predictable monthly costs." &
gen 6 "Want to compare 2027 Medigap rates in your area? Comment GUIDE below, and we will send you our free Medicare comparison." &
wait

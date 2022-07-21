local building_w_feet   = 8
local building_w_inch   = 1
local building_w_inch_n = 1
local building_w_inch_d = 2

local building_l_feet   = 28
local building_l_inch   = 4
local building_l_inch_n = 5
local building_l_inch_d = 16

local ridge_w_inch      = 1
local ridge_w_n         = 1
local ridge_w_d         = 2
                             ------  / "hip"
local roof_type   = "common" -- also: "valley"
                             ------  \ "shed"

local soffit            = 9
	
local roof_pitch        = 9
local smallest_denom    = 16

print()

local function round(n, d)
    local mult = 10 ^ (d or 0)
    return math.floor(n * mult + 0.5) / mult
end

local function simplify(n, d)
    nn, nd = n, d
    ret = 0
    while(d > 0) do
        ret = d
        n, d = d, n % d
    end
    return round(nn / ret).."/".. round(nd / ret)
end

local function ft_to_in(f)
    return f * 12
end

local function in_to_ft(i)
    return math.floor(i / 12)
end

local function frac_to_dec(n, d)
    return n / d
end

local function dec_to_frac(d)
    local w, smallest_denom = 0, smallest_denom
    if (d >= 1) then
        w = math.floor(d)
        d = d - w
    end
    local numer = math.floor(round(d * smallest_denom))
    
    return tostring(w.." "..numer.."/"..smallest_denom)
end

local function format_measurement(n)
    local feet = in_to_ft(n)
    n = n - (feet * 12)
    local inch = dec_to_frac(n)
    return feet.."' "..inch.."in"
end

local building_w =
    ft_to_in(building_w_feet) +
    building_w_inch +
    frac_to_dec(building_w_inch_n,
    building_w_inch_d)
    
local rise_ratio = roof_pitch / 12
local run = (building_w / 2) - 
	((ridge_w_inch +
		frac_to_dec(ridge_w_n, ridge_w_d)) / 2)
local rise = run * rise_ratio

local rafter_length_to_wall = math.sqrt(run ^ 2 + rise ^ 2)
local rafter_length_with_tail = math.sqrt((run + soffit) ^ 2 + rise ^ 2)

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("Building length: "..building_w_feet.."ft "..building_w_inch.." "..building_w_inch_n.."/"..building_w_inch_d.."in")
print("Rise ("..roof_pitch.."inch pitch): "..format_measurement(rise))
print("Run: "..format_measurement(run))
print("\nRafter length to outside of wall\n(shoulder cut): "
	..format_measurement(rafter_length_to_wall))
print("Rafter length including tails: "
	..format_measurement(rafter_length_with_tail))
print("\nThe ridge beam was been accounted for.\n"
	.."Will still need to subtract\nfrom tails for fascia board "
	.."and trim.")
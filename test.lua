function ft_to_in(f)
    return f * 12
end

function in_to_ft(i)
    return math.floor(i / 12), i % 12
end

function frac_to_dec(n, d)
    return n / d
end
    

function dec_to_frac(d)
    local d, w, denom = d, 0, denom
    if (d >= 1) then
        w = math.floor(d)
        d = d - w
    end
    numer = round(d * denom)
    
    return tostring(w.."&"..simplify(numer, denom))
end

ft, inch = in_to_ft(370)

print(ft.."ft "..inch.."in")
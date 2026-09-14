import { cp, mkdir } from "node:fs/promises";
import { readFileSync } from "node:fs";
import { resolve, join } from "node:path";
import { fileURLToPath } from "node:url";
const source = fileURLToPath(new URL("../", import.meta.url));
const output = resolve(process.argv[2] || "public/template-assets");
const rows = JSON.parse(readFileSync(join(source,"catalog.json"),"utf8"));
for (const row of rows) {
 if (!row.logo) continue;
 const match = /^\/template-assets\/([a-z0-9.-]+)\/(logo\.(?:svg|png|webp|jpe?g))$/.exec(row.logo);
 if (!match || match[1] !== row.id) throw new Error("Invalid catalog asset path: " + row.id);
 const target = join(output, row.id);
 await mkdir(target,{recursive:true});
 await cp(join(source,"blueprints",row.id,match[2]),join(target,match[2]));
}
